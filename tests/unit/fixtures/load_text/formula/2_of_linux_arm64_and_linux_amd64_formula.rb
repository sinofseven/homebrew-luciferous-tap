class OidcJwksConverter < Formula
  desc "Convert OIDC JWKS public keys to PEM format"
  homepage "https://github.com/sinofseven/oidc-jwks-converter"
  version "0.1.0"
  license "MIT"

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/oidc-jwks-converter/releases/download/v0.1.0/oidc-jwks-converter_v0.1.0_aarch64-unknown-linux-musl.zip"
      sha256 "92c1bb7eec43082aa45ebc3a776347cbabe692d13fb01c2798ce9de263a70bf7"
    end
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
