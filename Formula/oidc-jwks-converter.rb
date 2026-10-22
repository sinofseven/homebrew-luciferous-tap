class OidcJwksConverter < Formula
  desc "CLI tool to extract and convert OIDC public keys to PEM certificate format"
  homepage "https://github.com/sinofseven/oidc-jwks-converter"
  version "v0.2.1"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/archive/refs/tags/v0.2.2.tar.gz"
      sha256 "6317257e10e11fee49b2c7d2a119c921aeeb59b3e57b83edb4a98b36d2ebd0af"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.1/oidc-jwks-converter_v0.2.1_aarch64-unknown-linux-musl.zip"
      sha256 "f8e7c0b582f042ae35d8ad0206a04251d0e4befc793e9253c2b0f6a7b602d75b"
    end
    on_intel do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.1/oidc-jwks-converter_v0.2.1_x86_64-unknown-linux-musl.zip"
      sha256 "9bb6315260cef82b652e28a25434e5ffd55622a058984ba735551d04877fe153"
    end
  end

  def install
    bin.install "oidc-jwks-converter"
  end

  test do
    system "#{bin}/oidc-jwks-converter", "--version"
  end
end
