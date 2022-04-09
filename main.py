def on_forever():
    basic.show_number(1)
    basic.show_leds("""
        #####
                #####
                #####  
                #####
                #####
    """)
basic.forever(on_forever)
