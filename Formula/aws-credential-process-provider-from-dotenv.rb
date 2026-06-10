class AwsCredentialProcessProviderFromDotenv < Formula
  desc "AWS credential provider from .env files for AWS CLI credential_process"
  homepage "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv"
  version "v0.2.0"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv/releases/download/v0.2.0/aws-credential-process-provider-from-dotenv_v0.2.0_aarch64-apple-darwin.zip"
      sha256 "3b0954e0e97d59fb396269bb5f57e379575136ffed3223c34716348e1959ebb8"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv/releases/download/v0.2.0/aws-credential-process-provider-from-dotenv_v0.2.0_aarch64-unknown-linux-musl.zip"
      sha256 "3ec7e15f4f3df40f8ed7d9cbeb586630f2106901f0537071bcc39afd8415d7fe"
    end
    on_intel do
      url "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv/releases/download/v0.2.0/aws-credential-process-provider-from-dotenv_v0.2.0_x86_64-unknown-linux-musl.zip"
      sha256 "e2868e97a834053d87e9abc21f68a85f3a8f778b05f9430aa79ed46c1aff81c9"
    end
  end

  def install
    bin.install "aws-credential-process-provider-from-dotenv"
  end

  test do
    system "#{bin}/aws-credential-process-provider-from-dotenv", "--version"
  end
end
