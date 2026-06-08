package console.app;

import console.utils.ValidCommands;

import static console.Main.log;

public class ConsoleAppUtils {
    public static void handleCommand(String input) {
        if (input.isEmpty())
            return;

        if (input.equals("help")) {
            log("Available commands: " + String.join(", ", ValidCommands.ALL_COMMANDS));
            return;
        }

        // Check menu base commands
        for (String command : ValidCommands.MENU_COMMANDS) {
            if (input.startsWith(command)) {
                String gameName = getRemainder(input, command);
                switch (command) {
                    case "start" -> {
                        StringBuilder capitalizedGameName = new StringBuilder();

                        for (String word : gameName.trim().split("\\s+")) {
                            if (!word.isEmpty()) {
                                capitalizedGameName
                                        .append(word.substring(0, 1).toUpperCase())
                                        .append(word.substring(1).toLowerCase())
                                        .append(" ");
                            }
                        }

                        gameName = capitalizedGameName.toString().trim();
                        report("New game started: " + (!gameName.trim().isEmpty() ? gameName : "Game " + ConsoleApp.guid++));
                    }
                    case "delete" -> report("Deleted game: " + gameName);

                    case "games" -> {
                        ConsoleApp consoleApp =  new ConsoleApp();
                        report("Games list: " + consoleApp.getGames().toString());
                    }
                }
                return;
            }
        }
        log("Executed base command: " + input);

    }

    private static String getRemainder(String input, String command) {
        if (input.length() <= command.length()) {
            return ""; // no remainder
        }

        return input.substring(command.length()).trim();
    }

    private static int stars = 5;
    private static int score = 500;
    private static int turn = 0;
    private static final String tabulators = "\t\t\t\t\t\t\t\t";

    private static void report() {
        log("|--- " + stars + " stars | " + score + " score | " + turn + "th turn" + " ---|" + tabulators + "\n");
    }

    private static void report(String message) {
        log("|--- " + stars + " stars | " + score + " score | " + turn + "th turn" + " ---|" + tabulators + "\n" + message);
    }
}
