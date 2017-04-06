/**
 * Created by sTux
 * Dated April 5th, 2017
 * C Standard: C11 with GNU extensions
 * Compile Flags: -std=gnu11 -Wall -g -l pthreads
**/
#include "stack.h"


static stack_t *head;


void init(stack_t **stack, char *data) {
    *stack = (stack_t *)malloc(sizeof(stack_t));
    (*stack)->data = (char *)malloc(strlen(data));
    memcpy((*stack)->data, data, strlen(data));
    (*stack)->next = (*stack)->prev = NULL;
    head = *stack;
}


void push(stack_t **stack, char *data) {
    stack_t *tmp = (stack_t *)malloc(sizeof(stack_t));
    tmp->data = (char *)malloc(strlen(data));
    memcpy(tmp->data, data, strlen(data));
    tmp->next = *stack;
    tmp->prev = NULL;
    (*stack)->prev = tmp;
    *stack = tmp;
}


void pop(char **ret) {
    if(*ret == NULL)
        *ret = (char *)malloc(strlen(head->data));

    memcpy(*ret, head->data, strlen(head->data));
    free(head->data);
    stack_t *nxt = head->prev;
    free(head);
    head = nxt;
}