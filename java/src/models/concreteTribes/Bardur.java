package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Bardur extends AbstractTribe {
    protected Bardur() {
        super(Tech.HUNTING, 5, false, 1, 0, 0.8, 1, 1, 1, 1);
    }
}
