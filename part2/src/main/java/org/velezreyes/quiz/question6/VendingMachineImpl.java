package org.velezreyes.quiz.question6;

import java.util.Map;
import java.util.HashMap;

public class VendingMachineImpl implements VendingMachine {
    private int insertedMoney;
    private Map<String, Drink> availableDrinks;
    private static final int COST_OF_DRINK = 50;

    public VendingMachineImpl() {
        this.insertedMoney = 0;
        this.availableDrinks = new HashMap<>();
        availableDrinks.put("Coca-Cola", new DrinkImpl("Coca-Cola", true));
        availableDrinks.put("Pepsi", new DrinkImpl("Pepsi", true));
    }

    @Override
    public void insertQuarter() {
        this.insertedMoney += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        Drink selectedDrink = availableDrinks.get(name);
        if (selectedDrink == null) {
            throw new UnknownDrinkException();
        }

        if (insertedMoney < COST_OF_DRINK) {
            throw new NotEnoughMoneyException();
        }

        insertedMoney -= COST_OF_DRINK;

        return selectedDrink;
    }

    public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }
}