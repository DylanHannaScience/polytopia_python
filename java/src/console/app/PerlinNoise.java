package console.app;

import java.util.Random;

public class PerlinNoise {

    private final int[] permutation = new int[512];

    public PerlinNoise(long seed) {
        int[] p = new int[256];
        for (int i = 0; i < 256; i++) {
            p[i] = i;
        }

        Random rand = new Random(seed);
        for (int i = 255; i > 0; i--) {
            int index = rand.nextInt(i + 1);
            int tmp = p[i];
            p[i] = p[index];
            p[index] = tmp;
        }

        for (int i = 0; i < 512; i++) {
            permutation[i] = p[i & 255];
        }
    }

    private static double fade(double t) {
        return t * t * t * (t * (t * 6 - 15) + 10);
    }

    private static double lerp(double t, double a, double b) {
        return a + t * (b - a);
    }

    private static double grad(int hash, double x, double y) {
        int h = hash & 7;
        double u = h < 4 ? x : y;
        double v = h < 4 ? y : x;
        return ((h & 1) == 0 ? u : -u) + ((h & 2) == 0 ? v : -v);
    }

    public double noise(double x, double y) {
        int X = (int) Math.floor(x) & 255;
        int Y = (int) Math.floor(y) & 255;

        x -= Math.floor(x);
        y -= Math.floor(y);

        double u = fade(x);
        double v = fade(y);

        int aa = permutation[X + permutation[Y]];
        int ab = permutation[X + permutation[Y + 1]];
        int ba = permutation[X + 1 + permutation[Y]];
        int bb = permutation[X + 1 + permutation[Y + 1]];

        return lerp(
                v,
                lerp(u, grad(aa, x, y), grad(ba, x - 1, y)),
                lerp(u, grad(ab, x, y - 1), grad(bb, x - 1, y - 1))
        );
    }
}
