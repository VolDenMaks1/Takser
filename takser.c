// Task tracker "Takser" C verion
#include <stdio.h>
#include <json-c/json.h>

int main(int argc, char *argv[])
{

    FILE *fp;

    char buffer[1024];

    struct tasks *tasks;
    struct tasks *text;
    struct tasks *status;
    struct tasks *id;

    fp = fopen("tasks.json", "r");
    fread(buffer, 1024, 1, fp);
    fclose(fp);

    tasks = json_tokener_parse(buffer);

    json_object_object_get_ex(tasks, "text", &text);
    json_object_object_get_ex(tasks, "text", &status);
    json_object_object_get_ex(tasks, "text", &id);

    if (argc < 2) {
        list_tasks();
        return 0;
    }
    else if (strcmp(argv[1], "add") == 0) 
    {
        add_task();
    }
    else if (strcmp(argv[1], "rm") == 0) 
    {
        remove_task();
    }
    else if (strcmp(argv[1], "d") == 0) 
    {
        done_task();
    }
    else if (strcmp(argv[1], "ip") == 0) 
    {
        in_progress_task();
    }
    else {
        printf("Unknown command: %s\n", argv[1]);
    }

}
    