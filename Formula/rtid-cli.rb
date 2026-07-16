class RtidCli < Formula
  desc "This is CLI Tool for generating Reversed Timestamp ID."
  homepage "https://github.com/sinofseven/rtid-cli"
  version "v0.2.0"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/rtid-cli/releases/download/v0.2.0/rtid_v0.2.0_aarch64-apple-darwin.zip"
      sha256 "387649b6b05200dc391c5a76bd32ca4f45143786559fb3e6b166b0d7855bbc77"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/rtid-cli/releases/download/v0.2.0/rtid_v0.2.0_aarch64-unknown-linux-musl.zip"
      sha256 "4137bb1ae3077a3f5384855ee3e947fbeac85f58fff5245df6013eb87e93c533"
    end
    on_intel do
      url "https://github.com/sinofseven/rtid-cli/releases/download/v0.2.0/rtid_v0.2.0_x86_64-unknown-linux-musl.zip"
      sha256 "80b7853c5528a9d54bb478d40603a025471a9c02ecfe8df6fe05ee0b1b4eb081"
    end
  end

  def install
    bin.install "rtid"
  end

  test do
    system "#{bin}/rtid", "--version"
  end
end
