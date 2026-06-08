package console;

import console.app.ConsoleApp;
import console.app.ConsoleAppUtils;
import console.app.main.DesktopApp;

import java.util.Objects;
import java.util.Scanner;

public class Main {

  public static void log(String message) {
    System.out.println(message);
  }

  static String farewellMessage = "Goodbye Mighty Ruler!";

  public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);

      /*
       * console app:
       */
      console(scanner);

      /*
       * desktop app:
       */
      createLoop(scanner, "desktop");
      exit(scanner);
  }

    private static void desktop(String choice) {
      DesktopApp desktopApp = new DesktopApp(choice);
    }

    private static void console(Scanner scanner) {
        ConsoleApp consoleApp = new ConsoleApp();
        createLoop(scanner, "console");
    }

    public static void exit(Scanner scanner) {
        log("Press any key to exit...");
        scanner.nextLine();
    }

    private static void createLoop(Scanner scanner, String appType) {
        if ("console".equals(appType)) {
            log("Polytopia CLI started. Type `start \"Game Name\"` or just `start` to start a new game.\n Example: start \"Misty Clouds\"\nType `help` to get the list of available commands.\n`exit` to quit.");
        } else {
            log("Polytopia Desktop app started. Press ENTER to start generating");
        }
      while (true) {
            System.out.print ("> ");
            String input = scanner.nextLine().trim();
            input = input.toLowerCase();

            if ("exit".equals(input) || "quit".equals(input)) {
                log(farewellMessage);
                return;
            }
            if ("console".equals(appType)) {
                ConsoleAppUtils.handleCommand(input);
            } else if ("desktop".equals(appType)) {
                log("""
                  Choose map type!
                  0 - Drylands
                  1 - Lakes
                  2- Conti
                  3 - Archi
                  4 - Water World""");
                String choice = scanner.nextLine();
                desktop(choice);
                log("Press ENTER to continue, type `exit` to quit.");
            }
        }
    }
}
