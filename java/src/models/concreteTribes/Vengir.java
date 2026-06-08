package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Vengir extends AbstractTribe {
    protected Vengir() {
        super(Tech.SMITHERY, 5, false, .1, 1, 1, .1, 1, 2, .1);
    }
}
