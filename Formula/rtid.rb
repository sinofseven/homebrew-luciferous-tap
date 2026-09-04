class Rtid < Formula
  desc "This is CLI Tool for generating Reversed Timestamp ID."
  homepage "https://github.com/sinofseven/rtid-cli"
  version "v0.2.1"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/sinofseven/rtid-cli/releases/download/v0.2.1/rtid_v0.2.1_aarch64-apple-darwin.zip"
      sha256 "d5ee2e302fa3cc692d780694ae8ebcbda886afa2a87dd9d62cfbae312c79778a"
    end
    on_intel do
      disable! date: "2026-05-15", because: "no x86_64 macOS binary is provided"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/sinofseven/rtid-cli/releases/download/v0.2.1/rtid_v0.2.1_aarch64-unknown-linux-musl.zip"
      sha256 "0fd54a0dfbf32950fbd57667ba8da9fd0ee4ea5014cd8ed6688f2aa722bfeed2"
    end
    on_intel do
      url "https://github.com/sinofseven/rtid-cli/releases/download/v0.2.1/rtid_v0.2.1_x86_64-unknown-linux-musl.zip"
      sha256 "b5fd0035b6bae0ce8eaa7930b83078f5838a66d130817d755a7588186c51c21d"
    end
  end

  def install
    bin.install "rtid"
  end

  test do
    system "#{bin}/rtid", "--version"
  end
end
