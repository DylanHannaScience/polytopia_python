package console.app.main;

enum MapType {
    DRYLANDS(.4, .0),
    LAKES(.1, .4),
        CONTI(.1,.52),
    ARCHI(.4, .56),
        WATER_WORLD(.4,.85); // TODO fix Water World

    public final double perlinScale;     // lower = larger regions
    public final double waterAndLandRatio;

    MapType(double ps, double walr) {
        this.perlinScale = ps;
        this.waterAndLandRatio = walr;
    }
}
