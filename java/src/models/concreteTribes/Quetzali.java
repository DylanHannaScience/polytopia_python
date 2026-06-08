package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Quetzali extends AbstractTribe {
    protected Quetzali() {
        super(Tech.STRATEGY, 7, false, 2, .1, 1, 1, 1, 1, 1);
    }
}
