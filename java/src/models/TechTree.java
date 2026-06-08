package models;

import java.util.*;

public final class TechTree {

    public static final Map<TechCategory, Map<Tech, List<Tech>>> TREE =
            Map.of(
                    TechCategory.WATER, Map.of(
                            Tech.FISHING, List.of(
                                    Tech.SAILING,
                                    Tech.NAVIGATION,
                                    Tech.AQUACULTURE,
                                    Tech.AQUATISM
                            )
                    ),
                    TechCategory.FOREST, Map.of(
                            Tech.HUNTING, List.of(
                                    Tech.ARCHERY,
                                    Tech.SPIRITUALISM,
                                    Tech.FORESTRY,
                                    Tech.MATHEMATICS
                            )
                    ),
                    TechCategory.MOBILITY, Map.of(
                            Tech.RIDING, List.of(
                                    Tech.ROADS,
                                    Tech.TRADE,
                                    Tech.FREE_SPIRIT,
                                    Tech.CHIVALRY
                            )
                    ),
                    TechCategory.LAND, Map.of(
                            Tech.ORGANIZATION, List.of(
                                    Tech.FARMING,
                                    Tech.CONSTRUCTION,
                                    Tech.STRATEGY,
                                    Tech.DIPLOMACY
                            )
                    ),
                    TechCategory.MOUNTAIN, Map.of(
                            Tech.CLIMBING, List.of(
                                    Tech.MINING,
                                    Tech.SMITHERY,
                                    Tech.MEDITATION,
                                    Tech.PHILOSOPHY
                            )
                    )
            );

    private TechTree() {}
}


enum TechCategory {
    WATER,
    FOREST,
    MOBILITY,
    LAND,
    MOUNTAIN
}

