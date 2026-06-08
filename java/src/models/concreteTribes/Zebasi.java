package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Zebasi extends AbstractTribe {
    protected Zebasi() {
        super(Tech.FARMING, 5, false, .5, 1, .5, 1, .5, 1, 1);
    }
}
