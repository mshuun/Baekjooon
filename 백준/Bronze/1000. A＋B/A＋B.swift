import Foundation

if let input = readLine() {
    let parts = input.split(separator: " ").compactMap { Int($0) }
    if parts.count == 2 {
        print(parts[0] + parts[1])
    }
}
