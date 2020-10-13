# Introduction

This is a basic recipe packaging the Leap-SDK with conan. At this moment it's meant to be used locally, since it's not clear how to automate the downloading process of the SDK's archive file.

# Usage

1. Download [SDK](https://developer.leapmotion.com/sdk-leap-motion-controller/). Unzip the archive file and set the ```LeapSDK_DIR``` environment variable e.g. on a Windows host like this:

```
setx LeapSDK_DIR=<ARCHIVE_DIR>
```

2. Run conan to create SDK packages for different configurations

```
python build.py
```

# Consuming ```leapsdk``` conan-package

Just include ```leapsdk/4.1.0``` in your conan recipe.