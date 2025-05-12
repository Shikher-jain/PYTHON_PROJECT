#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <gtk/gtk.h>

GtkWidget *entry;

void button_click(GtkWidget *widget, gpointer data) {
    int number = GPOINTER_TO_INT(data);
    char *current = gtk_entry_get_text(GTK_ENTRY(entry));
    char *new_text = malloc(strlen(current) + 2);
    sprintf(new_text, "%s%d", current, number);
    gtk_entry_set_text(GTK_ENTRY(entry), new_text);
    free(new_text);
}

void button_clear() {
    gtk_entry_set_text(GTK_ENTRY(entry), "");
}

void button_equal() {
    char *current = gtk_entry_get_text(GTK_ENTRY(entry));
    double result = eval(current);
    char *result_str = malloc(50);
    sprintf(result_str, "%f", result);
    gtk_entry_set_text(GTK_ENTRY(entry), result_str);
    free(result_str);
}

void button_backspace() {
    char *current = gtk_entry_get_text(GTK_ENTRY(entry));
    int len = strlen(current);
    if (len > 0) {
        char *new_text = malloc(len);
        strncpy(new_text, current, len - 1);
        new_text[len - 1] = '\0';
        gtk_entry_set_text(GTK_ENTRY(entry), new_text);
        free(new_text);
    }
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Simple Calculator");

    GtkWidget *grid = gtk_grid_new();
    gtk_container_add(GTK_CONTAINER(window), grid);

    entry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), entry, 0, 0, 3, 1);

    GtkWidget *button;
    int row = 1, col = 0;

    for (int i = 1; i <= 9; i++) {
        button = gtk_button_new_with_label(g_strdup_printf("%d", i));
        g_signal_connect(button, "clicked", G_CALLBACK(button_click), GINT_TO_POINTER(i));
        gtk_grid_attach(GTK_GRID(grid), button, col, row, 1, 1);
        col++;
        if (col > 2) {
            col = 0;
            row++;
        }
    }

    button = gtk_button_new_with_label("0");
    g_signal_connect(button, "clicked", G_CALLBACK(button_click), GINT_TO_POINTER(0));
    gtk_grid_attach(GTK_GRID(grid), button, 0, 4, 1, 1);

    button = gtk_button_new_with_label("+");
    g_signal_connect(button, "clicked", G_CALLBACK(button_click), GINT_TO_POINTER('+'));
    gtk_grid_attach(GTK_GRID(grid), button, 1, 4, 1, 1);

    button = gtk_button_new_with_label("=");
    g_signal_connect(button, "clicked", G_CALLBACK(button_equal), NULL);
    gtk_grid_attach(GTK_GRID(grid), button, 2, 4, 2, 1);

    button = gtk_button_new_with_label("-");
    g_signal_connect(button, "clicked", G_CALLBACK(button_click), GINT_TO_POINTER('-'));
    gtk_grid_attach(GTK_GRID(grid), button, 0, 5, 1, 1);

    button = gtk_button_new_with_label("*");
    g_signal_connect(button, "clicked", G_CALLBACK(button_click), GINT_TO_POINTER('*'));
    gtk_grid_attach(GTK_GRID(grid), button, 1, 5, 1, 1);

    button = gtk_button_new_with_label("/");
    g_signal_connect(button, "clicked", G_CALLBACK(button_click), GINT_TO_POINTER('/'));
    gtk_grid_attach(GTK_GRID(grid), button, 2, 5, 1, 1);

    button = gtk_button_new_with_label("Clear");
    g_signal_connect(button, "clicked", G_CALLBACK(button_clear), NULL);
    gtk_grid_attach(GTK_GRID(grid), button, 0, 6, 2, 1);

    button = gtk_button_new_with_label("<<");
    g_signal_connect(button, "clicked", G_CALLBACK(button_backspace), NULL);
    gtk_grid_attach(GTK_GRID(grid), button, 2, 6, 1, 1);

    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}

