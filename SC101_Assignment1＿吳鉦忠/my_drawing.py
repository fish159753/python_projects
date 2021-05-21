"""
File: my_drawing.py
Name: Andy Wu
----------------------
TODO:  The lazy deer laid on the ground.
       Like me, to relax for a while.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    The lazy deer laid on the ground.
    Like me, to relax for a while.
    """
    window = GWindow(605, 648)
    # nose
    trianglen = GPolygon()
    trianglen.add_vertex((308, 459))
    trianglen.add_vertex((307, 469))
    trianglen.add_vertex((314, 478))
    trianglen.add_vertex((325, 482))
    trianglen.add_vertex((339, 478))
    trianglen.add_vertex((346, 469))
    trianglen.add_vertex((345, 459))
    trianglen.color = "silver"
    trianglen.filled = True
    trianglen.fill_color = "silver"
    window.add(trianglen)

    trianglen1 = GPolygon()
    trianglen1.add_vertex((308, 459))
    trianglen1.add_vertex((307, 469))
    trianglen1.add_vertex((314, 478))
    trianglen1.add_vertex((308, 483))
    trianglen1.add_vertex((300, 474))
    trianglen1.color = "darkslategray"
    trianglen1.filled = True
    trianglen1.fill_color = "darkslategray"
    window.add(trianglen1)

    trianglen2 = GPolygon()
    trianglen2.add_vertex((339, 478))
    trianglen2.add_vertex((346, 469))
    trianglen2.add_vertex((345, 459))
    trianglen2.add_vertex((353, 474))
    trianglen2.add_vertex((346, 483))
    trianglen2.color = "darkslategray"
    trianglen2.filled = True
    trianglen2.fill_color = "darkslategray"
    window.add(trianglen2)

    # Left eye
    triangle1 = GPolygon()
    triangle1.add_vertex((258, 367))
    triangle1.add_vertex((248, 375))
    triangle1.add_vertex((251, 383))
    triangle1.add_vertex((262, 388))
    triangle1.add_vertex((279, 390))
    triangle1.add_vertex((282, 386))
    triangle1.add_vertex((277, 376))
    triangle1.add_vertex((266, 373))
    triangle1.color = "saddlebrown"
    triangle1.filled = True
    triangle1.fill_color = "saddlebrown"
    window.add(triangle1)

    triangle2 = GPolygon()
    triangle2.add_vertex((251, 383))
    triangle2.add_vertex((250, 400))
    triangle2.add_vertex((262, 388))
    triangle2.color = "lightsage"
    triangle2.filled = True
    triangle2.fill_color = "lightsage"
    window.add(triangle2)

    triangle3 = GPolygon()
    triangle3.add_vertex((250, 400))
    triangle3.add_vertex((262, 388))
    triangle3.add_vertex((280, 420))
    triangle3.color = "mediumaquamarine"
    triangle3.filled = True
    triangle3.fill_color = "mediumaquamarine"
    window.add(triangle3)

    triangle4 = GPolygon()
    triangle4.add_vertex((262, 388))
    triangle4.add_vertex((279, 390))
    triangle4.add_vertex((280, 420))
    triangle4.color = "mediumspringgreen"
    triangle4.filled = True
    triangle4.fill_color = "mediumspringgreen"
    window.add(triangle4)

    triangle5 = GPolygon()
    triangle5.add_vertex((250, 400))
    triangle5.add_vertex((244, 414))
    triangle5.add_vertex((280, 420))
    triangle5.color = "yellowgreen"
    triangle5.filled = True
    triangle5.fill_color = "yellowgreen"
    window.add(triangle5)

    triangle5 = GPolygon()
    triangle5.add_vertex((244, 414))
    triangle5.add_vertex((280, 420))
    triangle5.add_vertex((256, 454))
    triangle5.color = "darksage"
    triangle5.filled = True
    triangle5.fill_color = "darksage"
    window.add(triangle5)

    triangle6 = GPolygon()
    triangle6.add_vertex((280, 420))
    triangle6.add_vertex((256, 454))
    triangle6.add_vertex((263, 461))
    triangle6.color = "darkolivegreen"
    triangle6.filled = True
    triangle6.fill_color = "darkolivegreen"
    window.add(triangle6)

    triangle7 = GPolygon()
    triangle7.add_vertex((280, 420))
    triangle7.add_vertex((263, 461))
    triangle7.add_vertex((280, 458))
    triangle7.color = "sienna"
    triangle7.filled = True
    triangle7.fill_color = "sienna"
    window.add(triangle7)

    triangle8 = GPolygon()
    triangle8.add_vertex((280, 420))
    triangle8.add_vertex((290, 457))
    triangle8.add_vertex((280, 458))
    triangle8.color = "peru"
    triangle8.filled = True
    triangle8.fill_color = "peru"
    window.add(triangle8)

    triangle9 = GPolygon()
    triangle9.add_vertex((280, 420))
    triangle9.add_vertex((301, 422))  
    triangle9.add_vertex((290, 457))
    triangle9.color = "lightslategray"
    triangle9.filled = True
    triangle9.fill_color = "lightslategray"
    window.add(triangle9)

    triangle10 = GPolygon()
    triangle10.add_vertex((280, 420))
    triangle10.add_vertex((301, 422))
    triangle10.add_vertex((303, 401))
    triangle10.color = "darkgoldenrod"
    triangle10.filled = True
    triangle10.fill_color = "darkgoldenrod"
    window.add(triangle10)

    triangle10 = GPolygon()
    triangle10.add_vertex((280, 420))
    triangle10.add_vertex((282, 386))
    triangle10.add_vertex((303, 401))
    triangle10.color = "tan"
    triangle10.filled = True
    triangle10.fill_color = "tan"
    window.add(triangle10)

    triangle11 = GPolygon()
    triangle11.add_vertex((279, 390))
    triangle11.add_vertex((282, 386))
    triangle11.add_vertex((280, 420))
    triangle11.color = "sienna"
    triangle11.filled = True
    triangle11.fill_color = "sienna"
    window.add(triangle11)

    # right eye==========================================
    triangle1r = GPolygon()
    triangle1r.add_vertex((395, 367))
    triangle1r.add_vertex((406, 375))
    triangle1r.add_vertex((402, 383))
    triangle1r.add_vertex((391, 388))
    triangle1r.add_vertex((375, 390))
    triangle1r.add_vertex((372, 386))
    triangle1r.add_vertex((375, 376))
    triangle1r.add_vertex((387, 373))
    triangle1r.color = "saddlebrown"
    triangle1r.filled = True
    triangle1r.fill_color = "saddlebrown"
    window.add(triangle1r)

    triangle2r = GPolygon()
    triangle2r.add_vertex((402, 383))
    triangle2r.add_vertex((403, 400))
    triangle2r.add_vertex((391, 388))
    triangle2r.color = "lightsage"
    triangle2r.filled = True
    triangle2r.fill_color = "lightsage"
    window.add(triangle2r)

    triangle3r = GPolygon()
    triangle3r.add_vertex((403, 400))
    triangle3r.add_vertex((391, 388))
    triangle3r.add_vertex((373, 420))
    triangle3r.color = "mediumaquamarine"
    triangle3r.filled = True
    triangle3r.fill_color = "mediumaquamarine"
    window.add(triangle3r)

    triangle4r = GPolygon()
    triangle4r.add_vertex((391, 388))
    triangle4r.add_vertex((375, 390))
    triangle4r.add_vertex((373, 420))
    triangle4r.color = "mediumspringgreen"
    triangle4r.filled = True
    triangle4r.fill_color = "mediumspringgreen"
    window.add(triangle4r)

    triangle5r = GPolygon()
    triangle5r.add_vertex((403, 400))
    triangle5r.add_vertex((410, 414))
    triangle5r.add_vertex((373, 420))
    triangle5r.color = "yellowgreen"
    triangle5r.filled = True
    triangle5r.fill_color = "yellowgreen"
    window.add(triangle5r)

    triangle5r = GPolygon()
    triangle5r.add_vertex((410, 414))
    triangle5r.add_vertex((373, 420))
    triangle5r.add_vertex((398, 454))
    triangle5r.color = "darksage"
    triangle5r.filled = True
    triangle5r.fill_color = "darksage"
    window.add(triangle5r)

    triangle6r = GPolygon()
    triangle6r.add_vertex((373, 420))
    triangle6r.add_vertex((398, 454))
    triangle6r.add_vertex((391, 461))
    triangle6r.color = "darkolivegreen"
    triangle6r.filled = True
    triangle6r.fill_color = "darkolivegreen"
    window.add(triangle6r)

    triangle7r = GPolygon()
    triangle7r.add_vertex((373, 420))
    triangle7r.add_vertex((391, 461))
    triangle7r.add_vertex((373, 458))
    triangle7r.color = "sienna"
    triangle7r.filled = True
    triangle7r.fill_color = "sienna"
    window.add(triangle7r)

    triangle8r = GPolygon()
    triangle8r.add_vertex((373, 420))
    triangle8r.add_vertex((363, 457))
    triangle8r.add_vertex((373, 458))
    triangle8r.color = "peru"
    triangle8r.filled = True
    triangle8r.fill_color = "peru"
    window.add(triangle8r)

    triangle9r = GPolygon()
    triangle9r.add_vertex((373, 420))
    triangle9r.add_vertex((350, 422))
    triangle9r.add_vertex((363, 457))
    triangle9r.color = "lightslategray"
    triangle9r.filled = True
    triangle9r.fill_color = "lightslategray"
    window.add(triangle9r)

    triangle10r = GPolygon()
    triangle10r.add_vertex((373, 420))
    triangle10r.add_vertex((350, 422))
    triangle10r.add_vertex((348, 401))
    triangle10r.color = "darkgoldenrod"
    triangle10r.filled = True
    triangle10r.fill_color = "darkgoldenrod"
    window.add(triangle10r)

    triangle10r = GPolygon()
    triangle10r.add_vertex((373, 420))
    triangle10r.add_vertex((371, 386))
    triangle10r.add_vertex((348, 401))
    triangle10r.color = "tan"
    triangle10r.filled = True
    triangle10r.fill_color = "tan"
    window.add(triangle10r)

    triangle11r = GPolygon()
    triangle11r.add_vertex((375, 390))
    triangle11r.add_vertex((371, 386))
    triangle11r.add_vertex((373, 420))
    triangle11r.color = "sienna"
    triangle11r.filled = True
    triangle11r.fill_color = "sienna"
    window.add(triangle11r)

    # nose
    trianglen3 = GPolygon()          
    trianglen3.add_vertex((314, 478))
    trianglen3.add_vertex((325, 482))
    trianglen3.add_vertex((307, 483))
    trianglen3.color = "darkgray"    
    trianglen3.filled = True         
    trianglen3.fill_color = "darkgray"
    window.add(trianglen3)           
                                                            
    trianglen4 = GPolygon()
    trianglen4.add_vertex((325, 482))
    trianglen4.add_vertex((339, 478))
    trianglen4.add_vertex((345, 483))
    trianglen4.color = "darkgray"
    trianglen4.filled = True
    trianglen4.fill_color = "darkgray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((307, 483))
    trianglen4.add_vertex((325, 482))
    trianglen4.add_vertex((345, 483))
    trianglen4.add_vertex((326, 497))
    trianglen4.color = "maroon"
    trianglen4.filled = True                                           
    trianglen4.fill_color = "maroon"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((307, 496))
    trianglen4.add_vertex((307, 483))
    trianglen4.add_vertex((326, 497))
    trianglen4.color = "darkslategray"
    trianglen4.filled = True
    trianglen4.fill_color = "darkslategray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((345, 496))
    trianglen4.add_vertex((345, 483))
    trianglen4.add_vertex((326, 497))
    trianglen4.color = "darkslategray"
    trianglen4.filled = True
    trianglen4.fill_color = "darkslategray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((290, 457))
    trianglen4.add_vertex((307, 483))
    trianglen4.add_vertex((307, 496))
    trianglen4.add_vertex((296, 491))
    trianglen4.color = "dimgray"
    trianglen4.filled = True
    trianglen4.fill_color = "dimgray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((363, 457))
    trianglen4.add_vertex((345, 483))
    trianglen4.add_vertex((345, 496))
    trianglen4.add_vertex((356, 491))
    trianglen4.color = "dimgray"
    trianglen4.filled = True
    trianglen4.fill_color = "dimgray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((290, 457))
    trianglen4.add_vertex((307, 483))
    trianglen4.add_vertex((263, 461))
    trianglen4.color = "gray"
    trianglen4.filled = True
    trianglen4.fill_color = "gray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((363, 457))
    trianglen4.add_vertex((345, 483))
    trianglen4.add_vertex((391, 461))
    trianglen4.color = "gray"
    trianglen4.filled = True
    trianglen4.fill_color = "gray"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((248, 375))
    trianglen4.add_vertex((251, 383))
    trianglen4.add_vertex((250, 400))
    trianglen4.add_vertex((242, 424))
    trianglen4.add_vertex((209, 448))
    trianglen4.add_vertex((227, 378))
    trianglen4.color = "chocolate"
    trianglen4.filled = True
    trianglen4.fill_color = "chocolate"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((406, 375))
    trianglen4.add_vertex((402, 383))
    trianglen4.add_vertex((403, 400))
    trianglen4.add_vertex((410, 424))
    trianglen4.add_vertex((446, 448))
    trianglen4.add_vertex((427, 378))
    trianglen4.color = "chocolate"
    trianglen4.filled = True
    trianglen4.fill_color = "chocolate"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((209, 449))
    trianglen4.add_vertex((243, 425))
    trianglen4.add_vertex((215, 480))
    trianglen4.color = "sandybrown"
    trianglen4.filled = True
    trianglen4.fill_color = "sandybrown"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((446, 448))
    trianglen4.add_vertex((437, 480))
    trianglen4.add_vertex((410, 425))
    trianglen4.color = "sandybrown"
    trianglen4.filled = True
    trianglen4.fill_color = "sandybrown"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((243, 425))
    trianglen4.add_vertex((215, 480))
    trianglen4.add_vertex((263, 461))
    trianglen4.color = "olive"
    trianglen4.filled = True
    trianglen4.fill_color = "olive"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((437, 480))
    trianglen4.add_vertex((410, 425))
    trianglen4.add_vertex((391, 461))
    trianglen4.color = "olive"
    trianglen4.filled = True
    trianglen4.fill_color = "olive"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((240, 540))
    trianglen4.add_vertex((215, 480))
    trianglen4.add_vertex((263, 461))
    trianglen4.color = "goldenrod"
    trianglen4.filled = True
    trianglen4.fill_color = "goldenrod"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((437, 480))
    trianglen4.add_vertex((391, 461))
    trianglen4.add_vertex((415, 540))
    trianglen4.color = "goldenrod"
    trianglen4.filled = True
    trianglen4.fill_color = "goldenrod"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((240, 540))
    trianglen4.add_vertex((293, 478))
    trianglen4.add_vertex((263, 461))
    trianglen4.color = "darkgoldenrod"
    trianglen4.filled = True
    trianglen4.fill_color = "darkgoldenrod"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((360, 478))
    trianglen4.add_vertex((391, 461))
    trianglen4.add_vertex((415, 540))
    trianglen4.color = "darkgoldenrod"
    trianglen4.filled = True
    trianglen4.fill_color = "darkgoldenrod"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((326, 515))
    trianglen4.add_vertex((307, 496))
    trianglen4.add_vertex((345, 496))
    trianglen4.color = "wheat"
    trianglen4.filled = True
    trianglen4.fill_color = "wheat"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((240, 540))
    trianglen4.add_vertex((293, 478))
    trianglen4.add_vertex((326, 515))
    trianglen4.color = "darkgoldenrod"
    trianglen4.filled = True
    trianglen4.fill_color = "darkgoldenrod"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((360, 478))
    trianglen4.add_vertex((326, 515))
    trianglen4.add_vertex((415, 540))
    trianglen4.color = "darkgoldenrod"
    trianglen4.filled = True
    trianglen4.fill_color = "darkgoldenrod"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((240, 540))
    trianglen4.add_vertex((326, 515))
    trianglen4.add_vertex((415, 540))
    trianglen4.color = "darkorange"
    trianglen4.filled = True
    trianglen4.fill_color = "darkorange"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((328, 459))
    trianglen4.add_vertex((290, 457))
    trianglen4.add_vertex((301, 422))
    trianglen4.color = "burlywood"
    trianglen4.filled = True
    trianglen4.fill_color = "burlywood"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((328, 459))
    trianglen4.add_vertex((363, 457))
    trianglen4.add_vertex((350, 422))
    trianglen4.color = "burlywood"
    trianglen4.filled = True
    trianglen4.fill_color = "burlywood"
    window.add(trianglen4)

    trianglen4 = GPolygon()
    trianglen4.add_vertex((328, 459))
    trianglen4.add_vertex((363, 457))
    trianglen4.add_vertex((290, 457))
    trianglen4.color = "burlywood"
    trianglen4.filled = True
    trianglen4.fill_color = "burlywood"
    window.add(trianglen4)


















































if __name__ == '__main__':
    main()
