package com.team.randominteger;

import javafx.event.ActionEvent;
import javafx.geometry.HPos;
import javafx.geometry.Pos;
import javafx.geometry.VPos;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;

import java.time.format.DateTimeFormatter;

public class Generator {

    private TextField field;
    private Button button;
    private Label output;

    public Generator(GridPane pane){
        Label label1 = new Label("Maximum Integer Limit:");
        label1.setId("labeling");
        pane.add(label1, 0,0);
        GridPane.setHalignment(label1, HPos.CENTER);
        GridPane.setValignment(label1, VPos.CENTER);

        field = new TextField();
        field.setPrefColumnCount(5);
        field.setAlignment(Pos.CENTER);
        field.setId("io");
        pane.add(field, 0,1);
        GridPane.setHalignment(field, HPos.CENTER);
        GridPane.setValignment(field, VPos.CENTER);

        button = new Button("Random Integer Generated:");
        button.setId("labeling");
        button.setOnAction(actionEvent -> {
            long m = Long.parseLong(field.getText());
            output.setText(String.valueOf(generate(m)));
        });
        pane.add(button, 0, 2);
        GridPane.setHalignment(button, HPos.CENTER);
        GridPane.setValignment(button, VPos.CENTER);

        output = new Label();
        output.setId("io");
        pane.add(output, 0, 3);
        GridPane.setHalignment(output, HPos.CENTER);
        GridPane.setValignment(output, VPos.CENTER);
    }

    private long generate(long m){
        long x = System.currentTimeMillis();

        return ((x * 8121 + 28411) % 134456)%(m+1);
    }
}
