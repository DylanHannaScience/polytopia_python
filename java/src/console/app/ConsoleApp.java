package console.app;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

import static console.Main.log;

public class ConsoleApp {
  static int guid = 1;
  private List<String> games = new ArrayList<>();

  public ConsoleApp() {
    readGuidReference();
    readGames();
  }

  public List<String> getGames() {
      readGames();
      return games;
  }

  private void readGuidReference() {
      try (InputStream input = ConsoleApp.class.getResourceAsStream("/guidReference.txt")) {
          if (input == null) {
              log("guidReference.txt not found!");
              return;
          }
          log(input.toString());

          List<String> lines = new java.io.BufferedReader(
                  new java.io.InputStreamReader(input)
          ).lines().toList();

          log("Read in guid reference:");
          lines.forEach(System.out::println);

          guid = Integer.parseInt(lines.getFirst().trim());

      } catch (Exception e) {
          e.printStackTrace();
      }
  }

    private void readGames() {
        try (InputStream input = ConsoleApp.class.getResourceAsStream("/games.txt")) {
            if (input == null) {
                log("games.txt not found!");
                return;
            }

            List<String> lines = new java.io.BufferedReader(
                    new java.io.InputStreamReader(input)
            ).lines().toList();

            log("Read in games:");
            games.clear();
            games.addAll(lines);
            reportGames();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    public void reportGames() {
    games.forEach(System.out::println);
  }

}
