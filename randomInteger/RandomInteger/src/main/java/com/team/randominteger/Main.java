package com.team.randominteger;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

import java.io.IOException;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        GridPane pane = new GridPane();
        Generator gen = new Generator(pane);
        pane.setId("grid");
        pane.getStylesheets().add(getClass().getResource("formStyle.css").toExternalForm());

        pane.setAlignment(Pos.CENTER);
        Scene scene = new Scene(pane, 520, 240);
        stage.setTitle("Random Integer Generator");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
