class CaseConverter < Formula
  desc "Convert text between case styles: snake_case, camelCase, PascalCase, kebab-case and more."
  homepage "https://github.com/sinofseven/case-converter"
  version "v1.1.3"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/case-converter/releases/download/v1.1.3/case-converter_v1.1.3_aarch64-apple-darwin.zip"
      sha256 "7304b7cc9798b2e0e54c961a463de64dde8a2b716c5fd03910a61b016bf17027"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/case-converter/releases/download/v1.1.3/case-converter_v1.1.3_aarch64-unknown-linux-musl.zip"
      sha256 "bebf16358a166600cde983cba17da154d8538316c4da43fa7c6aebe1c8979c59"
    end
    on_intel do
      url "https://github.com/sinofseven/case-converter/releases/download/v1.1.3/case-converter_v1.1.3_x86_64-unknown-linux-musl.zip"
      sha256 "3e926e757bc72c03f1154c10099897814071f5e1ca899bf06419c2adaedf02b7"
    end
  end

  def install
    bin.install "case-converter"
  end

  test do
    system "#{bin}/case-converter", "--version"
  end
end
