#include "linux/module.h"
#include "linux/init.h"
#include "linux/kernel.h"
// #include "param.h"


// ******************************************************************************************

#define DRIVER_AUTHOR  "S1lent"
#define DRIVER_DESC    "Module: X Itter -> X_2290_A >> Chat module itter 1"

// -----------------------------------------------------------------------------------------

#define _gs   "\033[32m"
#define _rs   "\033[31m"
#define _ys   "\033[33m"
#define blue  "\033[34m"
#define _ce   "\033[0m"

// ******************************************************************************************
/* Module parameters -> Definitions */
static char *cmd_str = "<INSERT_COMMAND_HERE>";
static int itter_id = 0;   // Default

/* Module parameters */
module_param(cmd_str, charp, 0000);
module_param(itter_id, int, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);

/* Module parameter descriptions */
MODULE_PARM_DESC(itter_id, "The itteration ID to use to exec sys_itter_function protocol...");
MODULE_PARM_DESC(cmd_str, "Command line string to be executed...");   // Because why not


// ******************************************************************************************
static int __init mod_start(void){
    printk(KERN_INFO "\n%s[ INFO ]%s%s Initializing program modules...%s\n 1.",_gs,_ce,_ys,_ce);
    // Initialize the modules

    return 0;
}

static void __exit mod_end(void) {
    printk(KERN_INFO "\n%s[ INFO ]%s%s Module itteration complete, system loaded...%s\n",_gs,_ce,_ys,_ce);
}

module_init(mod_start);
module_exit(mod_end);

// Module description
MODULE_LICENSE("GPL");
MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_DESCRIPTION(DRIVER_DESC);
