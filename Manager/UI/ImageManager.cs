using dc.hxd;
using HaxeProxy.Runtime;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace DeadCellsArchipelago {
    public static class ImageManager
    {
        public static bool stopTryingToConvertRgbaToRgba = false;

        public static dc.h2d.Tile LoadTileFromPng(string path)
        {
            using var image = Image.Load<Rgba32>(path);
            int w = image.Width, h = image.Height;

            byte[] pixelBytes = new byte[w * h * 4];
            image.CopyPixelDataTo(pixelBytes);

            var hxPixelBytes = ToHaxeBytes(pixelBytes);

            int offset = 0;
            var pixels = new Pixels(w, h, hxPixelBytes, new PixelFormat.RGBA(), new Ref<int>(ref offset));

            stopTryingToConvertRgbaToRgba = true;
            var texture = dc.h3d.mat.Texture.Class.fromPixels.Invoke(pixels, null);
            var tile = dc.h2d.Tile.Class.fromTexture.Invoke(texture);

            pixels.dispose();
            return tile;
        }

        private static dc.haxe.io.Bytes ToHaxeBytes(byte[] data)
        {
            var hxBytes = dc.haxe.io.Bytes.Class.alloc.Invoke(data.Length);
            System.Runtime.InteropServices.Marshal.Copy(data, 0, hxBytes.b, data.Length);
            return hxBytes;
        }

        public static void OnConvert(Hook_Pixels.orig_convert orig, Pixels self, PixelFormat target)
        {
            if(stopTryingToConvertRgbaToRgba)
            {
                stopTryingToConvertRgbaToRgba = false;
                return;
            }
            orig(self, target);
        }

        public static string GetResPath(string name)
        {
            return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "res", name);;
        }
    }
}