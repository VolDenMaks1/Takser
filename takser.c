#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h> //Why is this showing an error?

// Maint task:
//     [x] Read the JSON file
//     [] Write the JSON file

typedef struct
{
    char text[1000];
    int status; // 0: not done, 1: in progress, 2: done
    int id;
} Task;

char * read_json(const char *filename)
{

    FILE *file = fopen(filename, "r"); // Opening file

    if (!file)
    { // Cheking if file is opened
        fprintf(stderr, "Error: Unable to open file %s\n", filename);
        return NULL;
    }

    fseek(file, 0, SEEK_END);  // Seeking to the end of the file
    long length = ftell(file); // Getting file length
    rewind(file);              // Going back to start point

    char *content = (char *)malloc(length + 1); // Allocating memory for content    (what does ths do?)

    if (!content)
    { // Checking if memory is allocated
        printf("Error: Unable to allocate memory\n");
        return NULL;
    }

    fread(content, 1, length, file); // Reading file content
    content[length] = '\0';          // Adding null character at the end of the content
    fclose(file);                    // Closing file
    return content;
} // Summary: This function reads the content of the file and returns it as a string (I dont know how it works I stole it from ChatGPT)

int main(int argc, char *argv[])
{
    //TEST CODE
    
    char *filename = "tasks.json";
    char *content = read_json(filename);

    if(!content)
    {
        return 1;
    }

    printf("%s\n", content);

    free(content);
}

//Ths project is to hard for me. But i will still try to do it.