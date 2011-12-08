# Hubot (Ted Dziuba's Fork)

This is a fork of GitHub's Hubot that's substantially less shitty.

For as much as GitHub tithes the Church of Unix, they really blew it on Hubot.
If you think about it, Hubot is a lot like old-school CGI. It takes text in
from an *adapter*, decides what to do with that request, and spits text back out.

Sound familiar? Yeah, because it's standard in/standard out. Unix can do that
all by itself with out all the stupid Node.js cancer.

This rewrite of Hubot accomplishes exactly that.

                                  +############+
                                  +## I HAVE ##+
        '$.` `$                   +## FOUND ###+
        @    ``$                  +## THE #####+
        :   ```$                  +## THINGS ##+
        $  ````$        '@@#      +##+''+''++#+#
        ```````$      @.$$$$$     +############+
        +'@.:.$#     .''+++@+:@   ++
           .:.      @$'@@@@''::  #+
           $@@      :$+++++''::  #
          $$$$::    @:::::@@@@@#
          $$$$:@    #'@$.$` $$::@
          $$$$:@ '$$$$` .  $$$$$$:
          ::@@@'+.$$$` . `$$@@':$:@
            :+  @.$$` . .':@'@@$:@@#
            @+  ':$` .  $$$$$$$$:@.'
            +$''$#  .  $$$:...$$::':
                  :  $$$$$: ``.$:: +@
                  @ $$$$$$:```.$::  $#
                   '$$$$$$$$$$:::#$$$$::
                    @@@:::::::''+ $$$$::
                       :''':'@    $$$$::
                       '+#:'+#    '$$$$'
                        @'@@'      ````
                         @@#
                         ''+
                         +'
                          #

            '.``````````````````````````.+

## Motivation

I wanted GH-Hubot to deploy some code, which, in my setup, amounts to running
`fab deploy`, and thought that Hubot would let me just run arbitrary shell commands,
and I was wrong. After looking into it, I decided that GH-Hubot is like, well,
anything people wore in the 80's. You're going to look back on that in a few years
and say "what the fuck was I *thinking*?".

Yeah, and GH-Hubot needs Redis. Why the fuck would you need bot-side persistence
so bad that you start a networked server to store it instead of using a file.

Want to do bot-side persistence with my Hubot? Go nuts, do what you will, but
write your own adapter/plugin for it.

## Getting Your Own

Dependencies you'll need:

  - bash
  - find

Basically the stuff you will find in a Unix/Linux distro worth using.


Some of the plugins and adapters have additional dependencies, most notably,
the campfire adapter needs Python and the `pip` package "pyfire", which you can get
by running `sudo pip install pyfire`.


## Run Hubot

Run Hubot for Campfire:

```console
export HUBOT_CAMPFIRE_SUBDOMAIN=xxx
export HUBOT_CAMPFIRE_PASSWORD=xxx
export HUBOT_CAMPFIRE_ROOM=xxx
export HUBOT_CAMPFIRE_USERNAME=xxx
bin/hubot -a campfire
```

Or just run it in shell"

```console
bin/hubot
```


## Adapters

My Hubot ships with both Campfire and shell adapters.

### Creating an Adapter

Way easier here than with GitHub's Hubot. Plus, you don't have to dirty your hands with JavaScript.

An **adapter** in this fork of Hubot is an arbitrary program. It's best to make it a shell
script, because you get to use the `list_plugins` bash function. Have a look at the
shell adapter for a basic example.

`list_plugins` will return a list of paths to plugin binaries, which you can call as you see fit.

## Scripts (Plugins)

Again, easier and more flexible than GH-Hubot. A plugin here is an arbitrary executable.

The preferred idiom is that every plugin gets executed for every line of input. If your plugin
has nothing to say for that input line, it should say nothing and exit normally. If it wants
to respond, it should print its response on standard out.

The adapter will read that response and do what it pleases with it.

Check out the `campfire` adapter for an example of how to execute plugins in parallel.

One cool feature that the Unix version of Hubot has that the Node.js version
does not is that, to add a plugin, you just need to put the executable in the
plugins directory. You do not need to restart Hubot.
