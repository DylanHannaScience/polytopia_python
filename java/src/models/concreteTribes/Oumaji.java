package models.concreteTribes;

import models.AbstractTribe;
import models.Tech;

public class Oumaji extends AbstractTribe {
    protected Oumaji() {
        super(Tech.RIDING, 6, false, 1, 1, .2, .2, .5, 1, 1);
    }
}
