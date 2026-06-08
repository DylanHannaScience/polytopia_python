package models;

import java.util.Objects;

public abstract class AbstractTribe {
    private Tech startingTech = null;
    private int startingStars = 5;
    private boolean isSpecial = false;

    private double fruitModifier = 1;
    private double cropModifier = 1;
    private double forestModifier = 1;
    private double wildAnimalModifier = 1;
    private double mountainModifier = 1;
    private double metalModifier = 1;
    private double fishModifier = 1;

    protected AbstractTribe(
            Tech startingTech,
            int startingStars,
            boolean isSpecial,
            double fruitModifier,
            double cropModifier,
            double forestModifier,
            double wildAnimalModifier,
            double mountainModifier,
            double metalModifier,
            double fishModifier
    ) {
        this.startingTech = startingTech;
        this.startingStars = startingStars;
        this.isSpecial = isSpecial;
        this.fruitModifier = fruitModifier;
        this.cropModifier = cropModifier;
        this.forestModifier = forestModifier;
        this.wildAnimalModifier = wildAnimalModifier;
        this.mountainModifier = mountainModifier;
        this.metalModifier = metalModifier;
        this.fishModifier = fishModifier;
    }

}
