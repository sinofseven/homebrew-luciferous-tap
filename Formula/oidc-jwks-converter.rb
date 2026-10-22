class OidcJwksConverter < Formula
  desc "CLI tool to extract and convert OIDC public keys to PEM certificate format"
  homepage "https://github.com/sinofseven/oidc-jwks-converter"
  version "v0.2.2"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.2/oidc-jwks-converter_v0.2.2_aarch64-apple-darwin.zip"
      sha256 "7c48da593b43e91a01dc91b81564f97af34bb86359abe704bf21be6b28d9d17f"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.2/oidc-jwks-converter_v0.2.2_aarch64-unknown-linux-musl.zip"
      sha256 "3eea6e1a96d8a8fb6235d7c159fc39ab86141e759870e0382b9a66a8b33266a9"
    end
    on_intel do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.2.2/oidc-jwks-converter_v0.2.2_x86_64-unknown-linux-musl.zip"
      sha256 "3080a3c3adf65c39ec8eb1c075fcb01dfc69038f1ae6790a7d925178aa487db3"
    end
  end

  def install
    bin.install "oidc-jwks-converter"
  end

  test do
    system "#{bin}/oidc-jwks-converter", "--version"
  end
end
