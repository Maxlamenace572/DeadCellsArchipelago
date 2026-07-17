using dc.h2d.col;
using dc.hxd;
using HaxeProxy.Runtime;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using Serilog;
using dc.ui.hud;

namespace DeadCellsArchipelago {
    public static class ImageManager
    {
        public static bool stopTryingToConvertRgbaToRgba = false;

        public static void InitializeImageHooks()
        {
            Log.Information("[AP] Loading Image Hooks...");
            
            Hook_Pixels.convert += OnConvert;

            Log.Information("[AP] Image Hooks loaded");
        }

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

        private static void OnConvert(Hook_Pixels.orig_convert orig, Pixels self, PixelFormat target)
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
            return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "res", name);
        }

        public static dc.h3d.Vector ColorVectorRGBA(double r, double g, double b, double A)
        {
            double R = r /255;
            double G = g /255;
            double B = b /255;
            return new dc.h3d.Vector(new Ref<double>(ref R), new Ref<double>(ref G), new Ref<double>(ref B), new Ref<double>(ref A));
        }

        public static void CenterX(dc.h2d.Object parent, dc.h2d.Object child)
        {
            Bounds boundsParent = parent.getSize(new Bounds());
            Bounds boundsChild = child.getSize(new Bounds());

            if (parent is Skill) child.x = ((boundsParent.xMax*((Skill) parent).get_pixelScale()) - boundsChild.xMax) /2;
            else child.x = (boundsParent.xMax - boundsChild.xMax) /2;
            child.posChanged = true;
        }

        public static void CenterX(int widthParent, dc.h2d.Object child)
        {
            Bounds boundsChild = child.getSize(new Bounds());
            child.x = (widthParent - boundsChild.xMax) /2;
            child.posChanged = true;
        }

        public static void CenterY(dc.h2d.Object parent, dc.h2d.Object child)
        {
            Bounds boundsParent = parent.getSize(new Bounds());
            Bounds boundsChild = child.getSize(new Bounds());
            if (parent is Skill) child.y = ((boundsParent.yMax*((Skill) parent).get_pixelScale()) - boundsChild.yMax) /2;
            else child.y = (boundsParent.yMax - boundsChild.yMax) /2;
            child.posChanged = true;
        }
    }
}