package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Imperius extends AbstractTribe {
    protected Imperius() {
        super(Tech.ORGANIZATION, 5, false, 2, 1, 1, .5, 1, 1, 1);
    }
}
