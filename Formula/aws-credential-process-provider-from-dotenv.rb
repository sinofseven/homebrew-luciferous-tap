class AwsCredentialProcessProviderFromDotenv < Formula
  desc "AWS credential provider from .env files for AWS CLI credential_process"
  homepage "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv"
  version "v0.2.1"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv/releases/download/v0.2.1/aws-credential-process-provider-from-dotenv_v0.2.1_aarch64-apple-darwin.zip"
      sha256 "71146e1de357372820c0194883579f5e9ddfe3acbeddeecfdf73cb588bb50a7a"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv/releases/download/v0.2.1/aws-credential-process-provider-from-dotenv_v0.2.1_aarch64-unknown-linux-musl.zip"
      sha256 "e5c05f9983eaa0e6e2710447d79f50784dff8b0e00e3e2132b179c8c17802384"
    end
    on_intel do
      url "https://github.com/sinofseven/aws-credential-process-provider-from-dotenv/releases/download/v0.2.1/aws-credential-process-provider-from-dotenv_v0.2.1_x86_64-unknown-linux-musl.zip"
      sha256 "8f4a0b40bfbbbffe82213937f23dbb5d39d90710dfce9efce2f4608f93f668a7"
    end
  end

  def install
    bin.install "aws-credential-process-provider-from-dotenv"
  end

  test do
    system "#{bin}/aws-credential-process-provider-from-dotenv", "--version"
  end
end
