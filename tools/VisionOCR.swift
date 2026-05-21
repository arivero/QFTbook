import Foundation
import Vision

struct OCRCandidate: Codable {
    let text: String
    let confidence: Float
}

struct OCRLine: Codable {
    let text: String
    let confidence: Float
    let candidates: [OCRCandidate]
    let boundingBox: [Double]
}

struct OCRPage: Codable {
    let image: String
    let lines: [OCRLine]
}

func recognize(path: String, languageCorrection: Bool) throws -> OCRPage {
    let url = URL(fileURLWithPath: path)
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = languageCorrection
    request.recognitionLanguages = ["en-US"]
    request.minimumTextHeight = 0.0

    let handler = VNImageRequestHandler(url: url, options: [:])
    try handler.perform([request])

    let observations = request.results ?? []
    let sorted = observations.sorted {
        let a = $0.boundingBox
        let b = $1.boundingBox
        if abs(a.midY - b.midY) > 0.015 {
            return a.midY > b.midY
        }
        return a.minX < b.minX
    }

    let lines = sorted.compactMap { observation -> OCRLine? in
        let candidates = observation.topCandidates(3).map {
            OCRCandidate(text: $0.string, confidence: $0.confidence)
        }
        guard let first = candidates.first else { return nil }
        let box = observation.boundingBox
        return OCRLine(
            text: first.text,
            confidence: first.confidence,
            candidates: candidates,
            boundingBox: [
                Double(box.minX),
                Double(box.minY),
                Double(box.width),
                Double(box.height)
            ]
        )
    }

    return OCRPage(image: path, lines: lines)
}

let args = CommandLine.arguments
var languageCorrection = false
var imagePaths: [String] = []

for arg in args.dropFirst() {
    if arg == "--language-correction" {
        languageCorrection = true
    } else {
        imagePaths.append(arg)
    }
}

if imagePaths.isEmpty {
    fputs("Usage: VisionOCR [--language-correction] image1.png [image2.png ...]\n", stderr)
    exit(2)
}

do {
    let pages = try imagePaths.map { try recognize(path: $0, languageCorrection: languageCorrection) }
    let encoder = JSONEncoder()
    encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
    let data = try encoder.encode(pages)
    FileHandle.standardOutput.write(data)
    FileHandle.standardOutput.write("\n".data(using: .utf8)!)
} catch {
    fputs("VisionOCR error: \(error)\n", stderr)
    exit(1)
}
