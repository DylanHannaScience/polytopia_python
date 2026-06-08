package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Hoodrick extends AbstractTribe {
    protected Hoodrick() {
        super(Tech.ARCHERY, 7, false, 1, 1, 1.5, 1, .5, 1, 1);
    }
}
