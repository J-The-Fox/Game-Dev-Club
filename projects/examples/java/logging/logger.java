package projects.examples.java.logging;

import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.time.LocalDateTime;

// Creating A Logging Class In Java Is Hard ;-;

public class logger {    

    String[] default_levels = {"BUG", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}; // The Levels Of Logging
    String[] default_log_format = {"date", "level", "message"}; // The Default Log Format

    // Constructor
    public logger(String date_format, String[] log_format, String[] levels_shown){
        date_time_format = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");

        // Check If The Levels Are Valid
        for (int i = 0; i < levels_shown.length; i++){
            if (Arrays.asList(default_levels).contains(levels_shown[i])){
            }
            else{
                System.out.println("Invalid level: " + levels_shown[i]);
                System.exit(1);
            }
        }

        // Check If The Log Format Is Valid
        for (int i = 0; i < log_format.length; i++){
            if (Arrays.asList(default_log_format).contains(log_format[i])){
            }
            else{
                System.out.println("Invalid log format: " + log_format[i]);
                System.exit(1);
            }
        }

        this.log_format = log_format;
        this.levels_shown = levels_shown;

        // LocalDateTime now = LocalDateTime.now();
        // System.out.println(date_time_format.format(now));
    }

    DateTimeFormatter date_time_format;
    String[] log_format;
    String[] levels_shown;

    public void write(String level, String message){
        if (Arrays.asList(levels_shown).contains(level)){
            LocalDateTime current_date_time = LocalDateTime.now();
            System.out.println(date_time_format.format(current_date_time) + " - [" + level + "]: " + message);
        }
    }
}