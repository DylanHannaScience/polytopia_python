package console.app.main;

import console.app.PerlinNoise;

import javax.swing.*;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;
import java.awt.*;
import java.util.*;
import java.util.List;

import static console.Main.exit;
import static console.Main.log;

public class DesktopApp {

    // Gameplay settings
    private static final int ROWS = 30;
    private static final int COLS = 30;
    private static final int NUMBER_OF_PLAYERS = 2;


    // Maptype and generation-related settings
    private static MapType mapType = MapType.LAKES;
    private static final double FOREST_RATE = .3;

    // Terrains
    private static final Color LAND = new Color(46, 168, 19);
    private static final Color FOREST = new Color(19, 85, 0);
    private static final Color OCEAN = Color.BLUE;
    private static final Color WATER = new Color(75, 208, 255); // not used yet
    private static final Color CAPITAL = new Color(0, 0, 0);
    private static final Color MOUNTAIN = new Color(133, 133, 133, 255);
    private static final Color VILLAGE = new Color(139, 75, 19);
    private static final Color RUIN = new Color(255, 255, 1, 230);

    private static final JPanel[][] tiles = new JPanel[ROWS][COLS];
    private static final Random random = new Random();

    // Statikus lista a kapitalok pozícióinak tárolására
    private static final List<Point> capitals = new ArrayList<>();
    // Statikus lista a hegyek pozícióinak tárolására
    private static final List<Point> mountains = new ArrayList<>();
    // Statikus lista a falvak pozícióinak tárolására
    private static final List<Point> villages = new ArrayList<>();

    public DesktopApp() {
        int mapType = 1;
        DesktopApp.mapType = MapType.values()[mapType];
        SwingUtilities.invokeLater(DesktopApp::createAndShowUI);
    }

    public DesktopApp(String choice) {
        log("DesktopApp mapType set to " + choice +
                " scale=" + mapType.perlinScale);
        int mapType = 0;
        try {
            mapType = Integer.parseInt(choice);
        } catch (NumberFormatException e) {
            exit(new Scanner(System.in));
        }
        DesktopApp.mapType = MapType.values()[mapType];
        SwingUtilities.invokeLater(DesktopApp::createAndShowUI);
    }

    private static void createAndShowUI() {
        log("Using PERLIN_SCALE=" + mapType.perlinScale +
                ", WATER_LAND_RATIO=" + mapType.waterAndLandRatio);
        JFrame frame = new JFrame("Polytopia");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel gridPanel = new JPanel(new GridLayout(ROWS, COLS)); // csinál egy ROWS * COLS méretű táblát
        PerlinNoise noise = new PerlinNoise(System.currentTimeMillis());

        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                JPanel tile = new JPanel();

                double value = noise.noise(
                        row * mapType.perlinScale,
                        col * mapType.perlinScale
                );

                double normalized = (value + 1) / 2.0; // zajgyártás

                tile.setBackground(normalized > mapType.waterAndLandRatio ? LAND : OCEAN); //  for archi
                boolean isForest = random.nextInt(100) / 100.0 < FOREST_RATE;
                if (isForest && tile.getBackground().equals(LAND)) {
                    tile.setBackground(FOREST);
                }
                tile.setBorder(BorderFactory.createLineBorder(Color.BLACK));

                tiles[row][col] = tile;
                gridPanel.add(tile);
            }
        }

        // 2️⃣ Place tribe capitals AFTER generation
        replaceTilesWithCities(NUMBER_OF_PLAYERS, CAPITAL);
        FillTheRestOfTheWorldWithVillages();
        GenerateMountains(); // pl. 10 hegy

        frame.add(gridPanel);
        frame.setSize(600, 600);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }


    /**
     * puts the given number of cities (capital or village) to the map with SOME STRICT RULES:
     * no city can be within minDistance tiles of the edge of the map or each other
     *
     * @param count number of cities to place
     * @param what  color to paint
     */
    private static void replaceTilesWithCities(int count, Color what) {
        int placed = 0;

        while (placed < count) {
            int row = random.nextInt(ROWS - 4) + 2; // At least 2 tiles from the edges and from other capitals
            int col = random.nextInt(COLS - 4) + 2;

            JPanel tile = tiles[row][col];

            if (tile.getBackground().equals(LAND) && isVillageFarEnough(row, col, capitals, 2)) {
                tile.setBackground(what);
                capitals.add(new Point(row, col)); // kapitalokat tároljuk ide
                placed++;
            }
        }
    }

    private static boolean isVillageFarEnough(int row, int col, List<Point> points, int minDistance) {
        for (Point p : points) {
            int dist = Math.abs(p.x - row) + Math.abs(p.y - col); // Manhattan distance
            if (dist < minDistance + 2) {
                return false; // túl közel
            }
        }
        return true; // jó hely
    }

    private static void GenerateMountains() {
        // total tiles = ROWS * COLS
        int totalTiles = ROWS * COLS;
        int count = totalTiles / 17 - capitals.size(); // alapértelmezett hegy szám

        if (count < 0) count = 0; // negatív érték esetén nulla

        GenerateMountains(count);
    }

    /**
     * fills the world with villages with SOME STRICT RULES:
     * finds the spots that are far enough (at least 2 tiles) from capitals and other villages.
     * Villages can spawn on water.
     *
     * @param count number of villages to place
     */
    private static void GenerateMountains(int count) {
        int placed = 0;

        while (placed < count) {
            int row = random.nextInt(ROWS - 4) + 2; // legalább 2 csempe távol a szélektől
            int col = random.nextInt(COLS - 4) + 2;

            JPanel tile = tiles[row][col];

            // Falvak bárhol lehetnek (víz vagy föld)
            // Viszont legalább 2 távol a kapitaloktól és a többi hegytől
            // Csak akkor állítsuk barna színűre, ha még nem capital vagy hegy
            Color bg = tile.getBackground();
            if (!bg.equals(OCEAN) && !bg.equals(CAPITAL) && !bg.equals(MOUNTAIN)) {
                tile.setBackground(MOUNTAIN);
                mountains.add(new Point(row, col));
                placed++;
            }

        }
    }

    private static void FillTheRestOfTheWorldWithVillages() {
        int increasingMagicNumber = 20;
        int totalTiles = ROWS * COLS;
        int villageCount = totalTiles / increasingMagicNumber - capitals.size();

        if (villageCount <= 0) {
            return;
        }

        List<Point> candidates = new ArrayList<>();

        // Collect all valid candidate tiles first
        for (int row = 1; row < ROWS - 1; row++) {
            for (int col = 1; col < COLS - 1; col++) {
                JPanel tile = tiles[row][col];
                Color bg = tile.getBackground();

                // Must be LAND or WATER and not already village, capital, mountain
                if (!bg.equals(LAND) && !bg.equals(OCEAN)) continue;

                // Check distance from capitals and mountains only (ignore villages here)
                if (!isVillageFarEnough(row, col, capitals, 2)) continue;

                candidates.add(new Point(row, col));
            }
        }

        // Shuffle candidate list for randomness
        Collections.shuffle(candidates, random);

        villages.clear();

        // Try to place as many villages as possible without violating distance to other villages
        for (Point candidate : candidates) {
            if (villages.size() >= villageCount) break;

            // Check distance to already placed villages
            if (!isVillageFarEnough(candidate.x, candidate.y, villages, 2)) {
                continue;
            }

            // Place village
            tiles[candidate.x][candidate.y].setBackground(VILLAGE);
            villages.add(candidate);
        }
    }
}
