class OidcJwksConverter < Formula
  desc "Convert OIDC JWKS public keys to PEM format"
  homepage "https://github.com/sinofseven/oidc-jwks-converter"
  version "0.1.0"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-apple-darwin.zip"
      sha256 "c3c38539a5e5cd41f84e39d65b20c7b17a1e39df940185cf4a42978d5fb364fc"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_intel do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_x86_64-unknown-linux-musl.zip"
      sha256 "45742af8a6628205348de0217953179a5f1580619e028e43d5ca154c13110588"
    end
  end

  def install
    bin.install "oidc-jwks-converter"
  end

  test do
    system "#{bin}/oidc-jwks-converter", "--version"
  end
end
