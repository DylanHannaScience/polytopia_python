package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Kickoo extends AbstractTribe {
    protected Kickoo() {
        super(Tech.FISHING, 5, false, 1, 1, 1, 1, .5, 1, .5);
    }
}
