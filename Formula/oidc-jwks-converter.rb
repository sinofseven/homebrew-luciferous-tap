class OidcJwksConverter < Formula
  desc "CLI tool to extract and convert OIDC public keys to PEM certificate format"
  homepage "https://github.com/sinofseven/oidc-jwks-converter"
  version "v0.2.0"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.0/oidc-jwks-converter_v0.2.0_aarch64-apple-darwin.zip"
      sha256 "02c0b6e10252bf715a67f5b4624bec1e2ee2e7d2cb6e8af191913a2c7999db4e"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.0/oidc-jwks-converter_v0.2.0_aarch64-unknown-linux-musl.zip"
      sha256 "b1ee97bc9e72fe93c1a08753cc724ea0633e1e2cdfd131c0db4ed683f6f46dc1"
    end
    on_intel do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.0/oidc-jwks-converter_v0.2.0_x86_64-unknown-linux-musl.zip"
      sha256 "cab3a822cd069b4192b6ad823340cd445bf7d6754685244de329e7dc3a386ac7"
    end
  end

  def install
    bin.install "oidc-jwks-converter"
  end

  test do
    system "#{bin}/oidc-jwks-converter", "--version"
  end
end
