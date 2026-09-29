# ================================================================
# NIGHT SHIFT
# ROUGH GAMEPLAY PROTOTYPE v9
#
# ================================================================
#
# BU SÜRÜMDE:
#
# - ÇÖP ARTIK MUTFAKTA BAŞTAN GÖRÜNÜR.
# - Çöp büyük siyah poşet şeklinde.
# - Görev sırası gelmeden alınamaz.
#
# - RESTORAN ÖN KAPISINI KİLİTLEMEK İÇİN ANAHTAR GEREKMİYOR.
# - Dışarı çık.
# - Kapıyı kapat.
# - Tekrar E bas.
# - Restoran kilitlenir.
#
# - ÜST RESTORAN ÇOK DAHA BÜYÜK.
# - MERDİVEN RESTORANIN İÇİNDE.
# - Merdivenin etrafında korkuluk var.
# - Daha fazla masa / sandalye var.
#
# - Dışarıda:
#       kaldırım
#       yol
#       karşı kaldırım
#       dumpster
#       binalar
#       sokak lambaları
#
# - Intro cinematic korunuyor.
# - Jumpscare korunuyor.
#
#
# STORY:
#
# 1. Intro
# 2. Mop'u al
# 3. 4 m² alanı F ile temizle
# 4. Elektrik kesilir
# 5. Post-it = 1143
# 6. Security computer = 1143
# 7. Kitchen'dan anahtarı al
# 8. Electrical Room'u anahtarla aç
# 9. Switch'e F
# 10. Elektrik gelir
# 11. Kitchen'daki çöpü al
# 12. Kırmızı merdiven kapısını anahtarla aç
# 13. Restoran salonuna çık
# 14. Ön kapıdan çık
# 15. Kapıyı kapat
# 16. E ile restoranı kilitle
# 17. Yolun karşısındaki dumpster'a git
# 18. Çöpü at
# 19. Final
# 20. Jumpscare
#
#
# JUMPSCARE:
#
# assets/images/jumpscare.png
#
#
# KONTROLLER:
#
# WASD  = Hareket
# Mouse = Bakış
# SPACE = Zıplama
# E     = Etkileşim
# F     = Mop / elektrik switch
# ESC   = Mouse bırak
# F10   = Çıkış
#
# ================================================================


from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from pathlib import Path


# ================================================================
# PROJE
# ================================================================

PROJECT_FOLDER = Path(__file__).parent

ASSETS_FOLDER = PROJECT_FOLDER / "assets"

application.asset_folder = ASSETS_FOLDER


# ================================================================
# APP
# ================================================================

app = Ursina()


window.title = "Night Shift"

window.borderless = False

window.fullscreen = False


window.color = color.rgb32(
    6,
    6,
    9
)


camera.background_color = color.rgb32(
    6,
    6,
    9
)


# ================================================================
# TEXTURE
# ================================================================

def safe_texture(path):

    try:

        loaded = load_texture(path)

        if loaded:

            return loaded

    except Exception as error:

        print(
            "[TEXTURE WARNING]",
            path,
            error
        )


    return "white_cube"


concrete_texture = safe_texture(
    "textures/environment/dirty_concrete/dirty_concrete_basecolor.jpg"
)


wood_texture = safe_texture(
    "textures/environment/oak_wood/oak_wood_basecolor.jpg"
)


metal_texture = safe_texture(
    "textures/environment/rusty_metal/rusty_metal_basecolor.jpg"
)


jumpscare_texture = safe_texture(
    "images/jumpscare.png"
)


# ================================================================
# COLORS
# ================================================================

WALL_COLOR = color.rgb32(
    105,
    101,
    98
)


FLOOR_COLOR = color.rgb32(
    62,
    60,
    59
)


CORRIDOR_COLOR = color.rgb32(
    52,
    51,
    52
)


CEILING_COLOR = color.rgb32(
    38,
    38,
    41
)


METAL_COLOR = color.rgb32(
    105,
    108,
    110
)


DARK_METAL = color.rgb32(
    55,
    58,
    60
)


WOOD_COLOR = color.rgb32(
    128,
    91,
    58
)


COUNTER_COLOR = color.rgb32(
    90,
    94,
    96
)


COUNTER_TOP_COLOR = color.rgb32(
    155,
    157,
    155
)


SKIN_COLOR = color.rgb32(
    205,
    158,
    120
)


KEY_COLOR = color.rgb32(
    255,
    198,
    30
)


TRASH_COLOR = color.rgb32(
    19,
    20,
    20
)


DUMPSTER_COLOR = color.rgb32(
    48,
    83,
    67
)


ROAD_COLOR = color.rgb32(
    35,
    37,
    39
)


SIDEWALK_COLOR = color.rgb32(
    112,
    109,
    104
)


RESTAURANT_WALL = color.rgb32(
    128,
    121,
    110
)


# ================================================================
# SKY
# ================================================================

sky = Sky(

    color=color.rgb32(
        8,
        8,
        12
    )
)


# ================================================================
# GAME STATE
# ================================================================

game_active = False

intro_playing = True

computer_mode = False

ending_started = False


current_interactable = None

current_door = None


NORMAL_SPEED = 4.4


# ================================================================
# STORY STATE
# ================================================================

has_mop = False

held_item = None


clean_progress = 0

clean_total = 4

cleaning_done = False


power_on = True


computer_unlocked = False


has_keys = False


electrical_switched_on = False


has_trash = False

trash_disposed = False


restaurant_locked = False


# ================================================================
# MAP SETTINGS
# ================================================================

WALL_HEIGHT = 3.60

WALL_THICKNESS = 0.25


DOOR_WIDTH = 1.55

DOOR_HEIGHT = 2.40


# ================================================================
# BASEMENT
# ================================================================

JAN_L = -12.0
JAN_R = -7.0
JAN_T = -8.0
JAN_B = -4.5


SEC_L = -11.6
SEC_R = -7.0
SEC_T = -4.5
SEC_B = 3.0


LOC_L = -7.0
LOC_R = 1.3
LOC_T = -8.0
LOC_B = -4.5


ELE_L = 1.3
ELE_R = 5.4
ELE_T = -8.0
ELE_B = -4.5


COR_L = -7.0
COR_R = 5.4
COR_T = -4.5
COR_B = 0.0


KIT_L = -7.0
KIT_R = 1.6
KIT_T = 0.0
KIT_B = 6.0


EMP_L = 1.6
EMP_R = 5.4
EMP_T = 0.0
EMP_B = 6.0


STA_L = 5.4
STA_R = 9.8
STA_T = -4.5
STA_B = 0.0


# ================================================================
# FLOOR
# ================================================================

def create_floor(
    left,
    right,
    top,
    bottom,
    floor_color=FLOOR_COLOR,
    y=-0.15,
    texture=None
):

    width = right - left

    depth = bottom - top


    if texture is None:

        texture = concrete_texture


    return Entity(

        model="cube",

        texture=texture,

        position=(

            (left + right) / 2,

            y,

            (top + bottom) / 2

        ),

        scale=(

            width,

            0.30,

            depth

        ),

        color=floor_color,

        collider="box"
    )


# ================================================================
# FLOOR AT HEIGHT
#
# surface_y = yürüdüğümüz yüzeyin yüksekliği.
# ================================================================

def create_floor_level(
    left,
    right,
    top,
    bottom,
    surface_y,
    floor_color,
    texture=None
):

    if texture is None:

        texture = concrete_texture


    return create_floor(

        left,

        right,

        top,

        bottom,

        floor_color=floor_color,

        y=surface_y - 0.15,

        texture=texture
    )


# ================================================================
# CEILING
# ================================================================

def create_ceiling(
    left,
    right,
    top,
    bottom,
    y=WALL_HEIGHT + 0.10
):

    return Entity(

        model="cube",

        texture=concrete_texture,

        position=(

            (left + right) / 2,

            y,

            (top + bottom) / 2

        ),

        scale=(

            right - left,

            0.30,

            bottom - top

        ),

        color=CEILING_COLOR,

        collider="box"
    )


# ================================================================
# WALL X
# ================================================================

def wall_x(
    start_x,
    end_x,
    z,
    base_y=0,
    height=WALL_HEIGHT,
    wall_color=WALL_COLOR
):

    width = end_x - start_x


    if width <= 0:

        return None


    return Entity(

        model="cube",

        texture=concrete_texture,

        position=(

            (start_x + end_x) / 2,

            base_y + height / 2,

            z

        ),

        scale=(

            width,

            height,

            WALL_THICKNESS

        ),

        color=wall_color,

        collider="box"
    )


# ================================================================
# WALL Z
# ================================================================

def wall_z(
    x,
    start_z,
    end_z,
    base_y=0,
    height=WALL_HEIGHT,
    wall_color=WALL_COLOR
):

    depth = end_z - start_z


    if depth <= 0:

        return None


    return Entity(

        model="cube",

        texture=concrete_texture,

        position=(

            x,

            base_y + height / 2,

            (start_z + end_z) / 2

        ),

        scale=(

            WALL_THICKNESS,

            height,

            depth

        ),

        color=wall_color,

        collider="box"
    )


# ================================================================
# X WALL DOOR
# ================================================================

def wall_x_door(
    start_x,
    end_x,
    z,
    door_x,
    base_y=0,
    wall_height=WALL_HEIGHT
):

    half = DOOR_WIDTH / 2


    wall_x(

        start_x,

        door_x - half,

        z,

        base_y=base_y,

        height=wall_height
    )


    wall_x(

        door_x + half,

        end_x,

        z,

        base_y=base_y,

        height=wall_height
    )


    upper_height = (

        wall_height
        -
        DOOR_HEIGHT

    )


    if upper_height > 0:

        Entity(

            model="cube",

            texture=concrete_texture,

            position=(

                door_x,

                base_y
                +
                DOOR_HEIGHT
                +
                upper_height / 2,

                z

            ),

            scale=(

                DOOR_WIDTH,

                upper_height,

                WALL_THICKNESS

            ),

            color=WALL_COLOR,

            collider="box"
        )


# ================================================================
# Z WALL DOOR
# ================================================================

def wall_z_door(
    x,
    start_z,
    end_z,
    door_z,
    base_y=0,
    wall_height=WALL_HEIGHT
):

    half = DOOR_WIDTH / 2


    wall_z(

        x,

        start_z,

        door_z - half,

        base_y=base_y,

        height=wall_height
    )


    wall_z(

        x,

        door_z + half,

        end_z,

        base_y=base_y,

        height=wall_height
    )


    upper_height = (

        wall_height
        -
        DOOR_HEIGHT

    )


    if upper_height > 0:

        Entity(

            model="cube",

            texture=concrete_texture,

            position=(

                x,

                base_y
                +
                DOOR_HEIGHT
                +
                upper_height / 2,

                door_z

            ),

            scale=(

                WALL_THICKNESS,

                upper_height,

                DOOR_WIDTH

            ),

            color=WALL_COLOR,

            collider="box"
        )


# ================================================================
# NOTIFICATION
# ================================================================

notification_panel = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        0.54,

        0.09

    ),

    position=(

        0,

        0.31

    ),

    color=color.rgba32(
        0,
        0,
        0,
        175
    ),

    enabled=False,

    z=1
)


notification_text = Text(

    parent=camera.ui,

    text="",

    origin=(0, 0),

    position=(

        0,

        0.305

    ),

    scale=0.94,

    color=color.white,

    enabled=False,

    z=0
)


def hide_notification():

    notification_panel.enabled = False

    notification_text.enabled = False


def show_notification(
    text,
    duration=2.5
):

    notification_text.text = text

    notification_panel.enabled = True

    notification_text.enabled = True


    invoke(

        hide_notification,

        delay=duration
    )


# ================================================================
# DOOR
# ================================================================

class SimpleDoor:

    def __init__(
        self,
        position,
        axis="x",
        door_color=color.rgb32(55, 100, 150),
        swing=-90,
        boarded=False,
        locked=False,
        name="DOOR",
        requires_power=False,
        final_lockable=False
    ):

        self.is_open = False

        self.swing = swing

        self.locked = locked

        self.name = name

        self.requires_power = requires_power

        self.final_lockable = final_lockable

        self.final_locked = False


        self.root = Entity(

            position=position
        )


        frame_color = color.rgb32(
            48,
            46,
            45
        )


        # ========================================================
        # X DOOR
        # ========================================================

        if axis == "x":

            Entity(

                parent=self.root,

                model="cube",

                position=(

                    -DOOR_WIDTH / 2,

                    DOOR_HEIGHT / 2,

                    0

                ),

                scale=(

                    0.12,

                    DOOR_HEIGHT,

                    0.20

                ),

                color=frame_color
            )


            Entity(

                parent=self.root,

                model="cube",

                position=(

                    DOOR_WIDTH / 2,

                    DOOR_HEIGHT / 2,

                    0

                ),

                scale=(

                    0.12,

                    DOOR_HEIGHT,

                    0.20

                ),

                color=frame_color
            )


            Entity(

                parent=self.root,

                model="cube",

                position=(

                    0,

                    DOOR_HEIGHT,

                    0

                ),

                scale=(

                    DOOR_WIDTH + 0.12,

                    0.12,

                    0.20

                ),

                color=frame_color
            )


            self.pivot = Entity(

                parent=self.root,

                position=(

                    -DOOR_WIDTH / 2 + 0.06,

                    0,

                    0

                )
            )


            self.leaf = Entity(

                parent=self.pivot,

                model="cube",

                position=(

                    (DOOR_WIDTH - 0.12) / 2,

                    DOOR_HEIGHT / 2,

                    0

                ),

                scale=(

                    DOOR_WIDTH - 0.12,

                    DOOR_HEIGHT - 0.10,

                    0.09

                ),

                texture=wood_texture,

                color=door_color,

                collider="box"
            )


        # ========================================================
        # Z DOOR
        # ========================================================

        else:

            Entity(

                parent=self.root,

                model="cube",

                position=(

                    0,

                    DOOR_HEIGHT / 2,

                    -DOOR_WIDTH / 2

                ),

                scale=(

                    0.20,

                    DOOR_HEIGHT,

                    0.12

                ),

                color=frame_color
            )


            Entity(

                parent=self.root,

                model="cube",

                position=(

                    0,

                    DOOR_HEIGHT / 2,

                    DOOR_WIDTH / 2

                ),

                scale=(

                    0.20,

                    DOOR_HEIGHT,

                    0.12

                ),

                color=frame_color
            )


            Entity(

                parent=self.root,

                model="cube",

                position=(

                    0,

                    DOOR_HEIGHT,

                    0

                ),

                scale=(

                    0.20,

                    0.12,

                    DOOR_WIDTH + 0.12

                ),

                color=frame_color
            )


            self.pivot = Entity(

                parent=self.root,

                position=(

                    0,

                    0,

                    -DOOR_WIDTH / 2 + 0.06

                )
            )


            self.leaf = Entity(

                parent=self.pivot,

                model="cube",

                position=(

                    0,

                    DOOR_HEIGHT / 2,

                    (DOOR_WIDTH - 0.12) / 2

                ),

                scale=(

                    0.09,

                    DOOR_HEIGHT - 0.10,

                    DOOR_WIDTH - 0.12

                ),

                texture=wood_texture,

                color=door_color,

                collider="box"
            )


        self.leaf.simple_door = self


        # ========================================================
        # BOARDED
        # ========================================================

        if boarded and axis == "x":

            for y_pos, angle in [

                (0.70, -7),

                (1.20, 5),

                (1.65, -4)

            ]:

                Entity(

                    parent=self.leaf,

                    model="cube",

                    position=(

                        0,

                        y_pos - DOOR_HEIGHT / 2,

                        -0.08

                    ),

                    rotation_z=angle,

                    scale=(

                        1.65,

                        0.15,

                        0.08

                    ),

                    texture=wood_texture,

                    color=color.rgb32(
                        105,
                        70,
                        40
                    )
                )


    # ============================================================
    # OPEN / CLOSE
    # ============================================================

    def toggle(self):

        if self.is_open:

            self.pivot.animate_rotation_y(

                0,

                duration=0.32,

                curve=curve.in_out_quad
            )


            self.is_open = False


        else:

            self.pivot.animate_rotation_y(

                self.swing,

                duration=0.32,

                curve=curve.in_out_quad
            )


            self.is_open = True


    # ============================================================
    # INTERACT
    # ============================================================

    def interact(self):

        global restaurant_locked


        # ========================================================
        # RESTAURANT FRONT DOOR FINAL LOCK
        #
        # ANAHTAR GEREKMİYOR.
        # ========================================================

        if self.final_lockable:

            if self.final_locked:

                show_notification(
                    "RESTAURANT IS LOCKED"
                )

                return


            # Ön kapının dış tarafı daha negatif Z.

            player_outside = (

                player.z

                <

                self.root.z - 0.35

            )


            # ----------------------------------------------------
            # Dışarıdayız + kapı kapalı.
            #
            # E = kilitle.
            #
            # ANAHTAR CHECK YOK.
            # ----------------------------------------------------

            if (

                player_outside

                and

                not self.is_open

            ):

                self.final_locked = True

                restaurant_locked = True


                show_notification(

                    "RESTAURANT LOCKED",

                    duration=2.5
                )


                update_tasks()

                return


        # ========================================================
        # NORMAL LOCKED DOORS
        # ========================================================

        if self.locked:

            if not has_keys:

                show_notification(

                    self.name
                    +
                    " IS LOCKED - KEY REQUIRED"

                )

                return


            if (

                self.requires_power

                and

                not power_on

            ):

                show_notification(

                    "NO POWER - RESTORE ELECTRICITY FIRST"

                )

                return


            self.locked = False


            show_notification(

                self.name
                +
                " UNLOCKED"

            )


            self.toggle()


            update_tasks()

            return


        self.toggle()


# ================================================================
# BASEMENT FLOORS
# ================================================================

create_floor(
    JAN_L,
    JAN_R,
    JAN_T,
    JAN_B
)


create_floor(
    SEC_L,
    SEC_R,
    SEC_T,
    SEC_B
)


create_floor(
    LOC_L,
    LOC_R,
    LOC_T,
    LOC_B
)


create_floor(
    ELE_L,
    ELE_R,
    ELE_T,
    ELE_B
)


create_floor(
    COR_L,
    COR_R,
    COR_T,
    COR_B,
    CORRIDOR_COLOR
)


create_floor(
    KIT_L,
    KIT_R,
    KIT_T,
    KIT_B
)


create_floor(
    EMP_L,
    EMP_R,
    EMP_T,
    EMP_B
)


create_floor(
    STA_L,
    STA_R,
    STA_T,
    STA_B,
    color.rgb32(
        48,
        47,
        47
    )
)


# ================================================================
# BASEMENT WALLS
# ================================================================

wall_x(
    JAN_L,
    JAN_R,
    JAN_T
)


wall_z(
    JAN_L,
    JAN_T,
    JAN_B
)


wall_x(
    JAN_L,
    JAN_R,
    JAN_B
)


wall_z(
    SEC_L,
    SEC_T,
    SEC_B
)


wall_x(
    SEC_L,
    SEC_R,
    SEC_B
)


wall_x(
    LOC_L,
    LOC_R,
    LOC_T
)


wall_x(
    ELE_L,
    ELE_R,
    ELE_T
)


wall_z(
    ELE_R,
    ELE_T,
    ELE_B
)


wall_z(
    KIT_L,
    KIT_T,
    KIT_B
)


wall_x(
    KIT_L,
    KIT_R,
    KIT_B
)


wall_z(
    EMP_R,
    EMP_T,
    EMP_B
)


wall_x(
    EMP_L,
    EMP_R,
    EMP_B
)


wall_z(
    KIT_R,
    KIT_T,
    KIT_B
)


# ================================================================
# BASEMENT DOORS
# ================================================================


# JANITOR

JANITOR_DOOR_Z = -6.25


wall_z_door(
    JAN_R,
    JAN_T,
    JAN_B,
    JANITOR_DOOR_Z
)


janitor_door = SimpleDoor(

    position=(

        JAN_R,

        0,

        JANITOR_DOOR_Z

    ),

    axis="z",

    door_color=color.rgb32(
        48,
        105,
        158
    ),

    swing=90,

    name="JANITOR DOOR"
)


# SECURITY

SECURITY_DOOR_Z = -1.85


wall_z_door(
    SEC_R,
    SEC_T,
    COR_B,
    SECURITY_DOOR_Z
)


security_door = SimpleDoor(

    position=(

        SEC_R,

        0,

        SECURITY_DOOR_Z

    ),

    axis="z",

    door_color=color.rgb32(
        48,
        105,
        158
    ),

    swing=-90,

    name="SECURITY DOOR"
)


wall_z(
    SEC_R,
    COR_B,
    SEC_B
)


# LOCKER

LOCKER_DOOR_X = -4.45


wall_x_door(
    LOC_L,
    LOC_R,
    LOC_B,
    LOCKER_DOOR_X
)


locker_door = SimpleDoor(

    position=(

        LOCKER_DOOR_X,

        0,

        LOC_B

    ),

    axis="x",

    door_color=color.rgb32(
        48,
        105,
        158
    ),

    swing=-90,

    name="LOCKER ROOM"
)


wall_z(
    LOC_R,
    LOC_T,
    LOC_B
)


# ELECTRICAL

ELE_DOOR_X = 3.70


wall_x_door(
    ELE_L,
    ELE_R,
    ELE_B,
    ELE_DOOR_X
)


electrical_door = SimpleDoor(

    position=(

        ELE_DOOR_X,

        0,

        ELE_B

    ),

    axis="x",

    door_color=color.rgb32(
        48,
        105,
        158
    ),

    swing=90,

    locked=True,

    name="ELECTRICAL ROOM"
)


# KITCHEN

KITCHEN_DOOR_X = -1.10


wall_x_door(
    KIT_L,
    KIT_R,
    KIT_T,
    KITCHEN_DOOR_X
)


kitchen_door = SimpleDoor(

    position=(

        KITCHEN_DOOR_X,

        0,

        KIT_T

    ),

    axis="x",

    door_color=color.rgb32(
        196,
        148,
        42
    ),

    swing=90,

    name="KITCHEN"
)


# EMPTY ROOM

EMPTY_DOOR_X = 3.60


wall_x_door(
    EMP_L,
    EMP_R,
    EMP_T,
    EMPTY_DOOR_X
)


empty_door = SimpleDoor(

    position=(

        EMPTY_DOOR_X,

        0,

        EMP_T

    ),

    axis="x",

    door_color=color.rgb32(
        95,
        66,
        43
    ),

    swing=-90,

    boarded=True,

    name="EMPTY ROOM"
)


# RED STAIR DOOR

STAIR_DOOR_Z = -2.20


wall_z_door(
    STA_L,
    STA_T,
    STA_B,
    STAIR_DOOR_Z
)


stairs_door = SimpleDoor(

    position=(

        STA_L,

        0,

        STAIR_DOOR_Z

    ),

    axis="z",

    door_color=color.rgb32(
        170,
        40,
        40
    ),

    swing=-90,

    locked=True,

    name="STAIR EXIT",

    requires_power=True
)


# ================================================================
# STAIR BASEMENT WALLS
# ================================================================

wall_z(
    STA_R,
    STA_T,
    STA_B
)


wall_x(
    STA_L,
    STA_R,
    STA_T
)


wall_x(
    STA_L,
    STA_R,
    STA_B
)


# ================================================================
# BASEMENT CEILINGS
# ================================================================

create_ceiling(
    JAN_L,
    JAN_R,
    JAN_T,
    JAN_B
)


create_ceiling(
    SEC_L,
    SEC_R,
    SEC_T,
    SEC_B
)


create_ceiling(
    LOC_L,
    LOC_R,
    LOC_T,
    LOC_B
)


create_ceiling(
    ELE_L,
    ELE_R,
    ELE_T,
    ELE_B
)


create_ceiling(
    COR_L,
    COR_R,
    COR_T,
    COR_B
)


create_ceiling(
    KIT_L,
    KIT_R,
    KIT_T,
    KIT_B
)


create_ceiling(
    EMP_L,
    EMP_R,
    EMP_T,
    EMP_B
)


# ================================================================
# JANITOR ROOM
# ================================================================

janitor_shelf = Entity(

    model="cube",

    texture=metal_texture,

    position=(

        -11.55,

        1.25,

        -6.55

    ),

    scale=(

        0.65,

        2.50,

        1.70

    ),

    color=DARK_METAL,

    collider="box"
)


for shelf_y in [

    0.65,

    1.30,

    1.95

]:

    Entity(

        model="cube",

        position=(

            -11.20,

            shelf_y,

            -6.55

        ),

        scale=(

            0.70,

            0.05,

            1.55

        ),

        color=METAL_COLOR
    )


janitor_cabinet = Entity(

    model="cube",

    texture=wood_texture,

    position=(

        -9.20,

        0.90,

        -7.55

    ),

    scale=(

        1.60,

        1.80,

        0.60

    ),

    color=color.rgb32(
        90,
        70,
        55
    ),

    collider="box"
)


bucket = Entity(

    model="cube",

    position=(

        -10.25,

        0.25,

        -7.25

    ),

    scale=(

        0.50,

        0.50,

        0.50

    ),

    color=color.rgb32(
        55,
        105,
        155
    )
)


# ================================================================
# MOP
# ================================================================

world_mop = Entity(

    position=(

        -10.35,

        0,

        -6.60

    )
)


Entity(

    parent=world_mop,

    model="cube",

    position=(

        0,

        0.80,

        0

    ),

    rotation_z=-8,

    scale=(

        0.07,

        1.60,

        0.07

    ),

    color=color.rgb32(
        130,
        105,
        70
    )
)


Entity(

    parent=world_mop,

    model="cube",

    position=(

        0.10,

        0.07,

        0

    ),

    scale=(

        0.65,

        0.14,

        0.35

    ),

    color=color.rgb32(
        205,
        205,
        190
    )
)


mop_hitbox = Entity(

    parent=world_mop,

    model="cube",

    position=(

        0,

        0.80,

        0

    ),

    scale=(

        0.70,

        1.70,

        0.55

    ),

    color=color.rgba32(
        0,
        0,
        0,
        0
    ),

    collider="box"
)


mop_hitbox.interaction_type = (
    "mop"
)


# ================================================================
# LOCKER ROOM
# ================================================================

bench = Entity(

    model="cube",

    texture=wood_texture,

    position=(

        -2.80,

        0.48,

        -6.55

    ),

    scale=(

        4.70,

        0.18,

        0.70

    ),

    color=WOOD_COLOR,

    collider="box"
)


rack_z = -7.45


Entity(

    model="cube",

    position=(

        -5.65,

        1.10,

        rack_z

    ),

    scale=(

        0.10,

        2.20,

        0.10

    ),

    color=DARK_METAL
)


Entity(

    model="cube",

    position=(

        -0.10,

        1.10,

        rack_z

    ),

    scale=(

        0.10,

        2.20,

        0.10

    ),

    color=DARK_METAL
)


Entity(

    model="cube",

    position=(

        -2.875,

        1.95,

        rack_z

    ),

    scale=(

        5.55,

        0.10,

        0.10

    ),

    color=DARK_METAL
)


for hook_x in [

    -5,

    -4,

    -3,

    -2,

    -1

]:

    Entity(

        model="cube",

        position=(

            hook_x,

            1.70,

            rack_z + 0.08

        ),

        rotation_z=25,

        scale=(

            0.05,

            0.38,

            0.05

        ),

        color=METAL_COLOR
    )


# ================================================================
# POST IT BOARD
# ================================================================

board_root = Entity(

    position=(

        -0.10,

        1.65,

        -4.67

    )
)


Entity(

    parent=board_root,

    model="cube",

    scale=(

        2.20,

        1.15,

        0.06

    ),

    texture=wood_texture,

    color=color.rgb32(
        112,
        71,
        40
    )
)


post_it_root = Entity(

    parent=board_root,

    position=(

        0.18,

        0,

        -0.06

    )
)


Entity(

    parent=post_it_root,

    model="cube",

    scale=(

        0.62,

        0.62,

        0.025

    ),

    color=color.rgb32(
        245,
        216,
        72
    )
)


# ================================================================
# POST IT 1143
# ================================================================

DIGITS = {

    "1": [
        "b",
        "c"
    ],

    "4": [
        "f",
        "g",
        "b",
        "c"
    ],

    "3": [
        "a",
        "b",
        "g",
        "c",
        "d"
    ]

}


def make_postit_digit(
    digit,
    x
):

    segments = {

        "a": (x, 0.15, 0),

        "g": (x, 0, 0),

        "d": (x, -0.15, 0),

        "f": (x - 0.07, 0.075, 90),

        "b": (x + 0.07, 0.075, 90),

        "e": (x - 0.07, -0.075, 90),

        "c": (x + 0.07, -0.075, 90)

    }


    for segment in DIGITS[digit]:

        sx, sy, angle = (
            segments[segment]
        )


        Entity(

            parent=post_it_root,

            model="cube",

            position=(

                sx,

                sy,

                -0.035

            ),

            rotation_z=angle,

            scale=(

                0.11,

                0.018,

                0.02

            ),

            color=color.rgb32(
                30,
                25,
                18
            )
        )


make_postit_digit(
    "1",
    -0.21
)

make_postit_digit(
    "1",
    -0.07
)

make_postit_digit(
    "4",
    0.07
)

make_postit_digit(
    "3",
    0.21
)


post_it_hitbox = Entity(

    parent=post_it_root,

    model="cube",

    scale=(

        0.70,

        0.70,

        0.08

    ),

    color=color.rgba32(
        0,
        0,
        0,
        0
    ),

    collider="box"
)


post_it_hitbox.interaction_type = (
    "note"
)


# ================================================================
# SECURITY
# ================================================================

security_desk = Entity(

    model="cube",

    texture=wood_texture,

    position=(

        -9.20,

        0.72,

        2.25

    ),

    scale=(

        3.60,

        1.44,

        0.80

    ),

    color=WOOD_COLOR,

    collider="box"
)


computer_body = Entity(

    model="cube",

    position=(

        -9.20,

        1.92,

        2.20

    ),

    scale=(

        1.25,

        0.88,

        0.14

    ),

    color=color.rgb32(
        30,
        32,
        30
    ),

    collider="box"
)


computer_body.interaction_type = (
    "computer"
)


computer_screen = Entity(

    model="quad",

    position=(

        -9.20,

        1.92,

        2.115

    ),

    rotation_y=180,

    scale=(

        1.05,

        0.68

    ),

    color=color.rgb32(
        25,
        75,
        52
    ),

    double_sided=True
)


# ================================================================
# ELECTRICAL
# ================================================================

electric_panel = Entity(

    model="cube",

    texture=metal_texture,

    position=(

        4.90,

        1.55,

        -6.20

    ),

    scale=(

        0.35,

        2.10,

        1.45

    ),

    color=DARK_METAL,

    collider="box"
)


electric_led = Entity(

    model="sphere",

    position=(

        4.61,

        2.20,

        -6.20

    ),

    scale=0.13,

    color=color.rgb32(
        60,
        220,
        80
    )
)


switch_lever = Entity(

    model="cube",

    position=(

        4.46,

        1.48,

        -6.20

    ),

    rotation_z=28,

    scale=(

        0.10,

        0.48,

        0.10

    ),

    color=color.rgb32(
        210,
        205,
        185
    )
)


switch_hitbox = Entity(

    model="cube",

    position=(

        4.38,

        1.50,

        -6.20

    ),

    scale=(

        0.38,

        1.10,

        0.90

    ),

    color=color.rgba32(
        0,
        0,
        0,
        0
    ),

    collider="box"
)


switch_hitbox.interaction_type = (
    "power_switch"
)


# ================================================================
# KITCHEN
# ================================================================

back_counter = Entity(

    model="cube",

    position=(

        -2.70,

        0.45,

        5.45

    ),

    scale=(

        7.00,

        0.90,

        0.75

    ),

    color=COUNTER_COLOR,

    collider="box"
)


Entity(

    model="cube",

    position=(

        -2.70,

        0.94,

        5.45

    ),

    scale=(

        7.10,

        0.08,

        0.82

    ),

    color=COUNTER_TOP_COLOR
)


left_counter = Entity(

    model="cube",

    position=(

        -6.45,

        0.45,

        3.40

    ),

    scale=(

        0.75,

        0.90,

        4.00

    ),

    color=COUNTER_COLOR,

    collider="box"
)


kitchen_island = Entity(

    model="cube",

    position=(

        -2.80,

        0.45,

        2.45

    ),

    scale=(

        3.40,

        0.90,

        1.15

    ),

    color=COUNTER_COLOR,

    collider="box"
)


# Fridge

Entity(

    model="cube",

    position=(

        0.65,

        1.05,

        5.35

    ),

    scale=(

        1.15,

        2.10,

        0.95

    ),

    color=color.rgb32(
        105,
        110,
        112
    ),

    collider="box"
)


# ================================================================
# KEY
# ================================================================

world_key = Entity(

    position=(

        -0.25,

        1.10,

        5.15

    ),

    enabled=False
)


Entity(

    parent=world_key,

    model="cube",

    position=(

        -0.27,

        0,

        0

    ),

    scale=(

        0.25,

        0.23,

        0.08

    ),

    color=KEY_COLOR
)


Entity(

    parent=world_key,

    model="cube",

    position=(

        0.08,

        0,

        0

    ),

    scale=(

        0.65,

        0.10,

        0.08

    ),

    color=KEY_COLOR
)


key_hitbox = Entity(

    parent=world_key,

    model="cube",

    scale=(

        1.0,

        0.50,

        0.50

    ),

    color=color.rgba32(
        0,
        0,
        0,
        0
    ),

    collider="box"
)


key_hitbox.interaction_type = (
    "keys"
)


# ================================================================
# ÇÖP
#
# ÖNEMLİ:
#
# ARTIK OYUNUN BAŞINDAN BERİ MUTFAKTA GÖRÜNÜR.
#
# Ama görev sırası gelmeden alamazsın.
# ================================================================

world_trash = Entity(

    position=(

        -5.55,

        0,

        4.75

    ),

    enabled=True
)


# Büyük ana poşet

Entity(

    parent=world_trash,

    model="cube",

    position=(

        0,

        0.43,

        0

    ),

    rotation=(

        4,

        8,

        -4

    ),

    scale=(

        0.78,

        0.85,

        0.70

    ),

    color=TRASH_COLOR
)


# Üst kısmı

Entity(

    parent=world_trash,

    model="cube",

    position=(

        0,

        0.93,

        0

    ),

    rotation_z=45,

    scale=(

        0.25,

        0.28,

        0.24

    ),

    color=color.rgb32(
        12,
        13,
        13
    )
)


# Küçük yan çıkıntı / poşet kırışıklığı

Entity(

    parent=world_trash,

    model="cube",

    position=(

        -0.32,

        0.40,

        0.10

    ),

    rotation_z=20,

    scale=(

        0.28,

        0.48,

        0.55

    ),

    color=color.rgb32(
        25,
        26,
        26
    )
)


trash_hitbox = Entity(

    parent=world_trash,

    model="cube",

    position=(

        0,

        0.50,

        0

    ),

    scale=(

        1.05,

        1.15,

        1.0

    ),

    color=color.rgba32(
        0,
        0,
        0,
        0
    ),

    collider="box"
)


trash_hitbox.interaction_type = (
    "trash"
)


# ================================================================
# CLEANING AREA
# ================================================================

clean_tiles = []


clean_positions = [

    (-2.75, -1.35),

    (-1.75, -1.35),

    (-2.75, -0.35),

    (-1.75, -0.35)

]


for stain_x, stain_z in clean_positions:

    stain = Entity(

        model="quad",

        position=(

            stain_x,

            0.015,

            stain_z

        ),

        rotation_x=90,

        scale=(

            0.92,

            0.92

        ),

        color=color.rgba32(
            105,
            22,
            20,
            220
        ),

        double_sided=True
    )


    clean_tiles.append(
        stain
    )


clean_marker = Entity(

    model="cube",

    position=(

        -2.25,

        0.55,

        -0.85

    ),

    rotation=(

        0,

        45,

        45

    ),

    scale=(

        0.20,

        0.20,

        0.20

    ),

    color=color.rgb32(
        245,
        215,
        70
    )
)


# ================================================================
# STAIRS
# ================================================================

STEP_COUNT = 10

STEP_HEIGHT = 0.18

STEP_RUN = 0.28

STAIR_WIDTH = 1.30


HALF_HEIGHT = (
    STEP_COUNT
    *
    STEP_HEIGHT
)


FULL_HEIGHT = (
    HALF_HEIGHT
    *
    2
)


# ================================================================
# LOWER FLIGHT
# ================================================================

lower_start_x = 5.75

lower_z = -0.95


for i in range(
    STEP_COUNT
):

    stair_height = (

        (i + 1)
        *
        STEP_HEIGHT

    )


    Entity(

        model="cube",

        texture=concrete_texture,

        position=(

            lower_start_x
            +
            i * STEP_RUN,

            stair_height / 2,

            lower_z

        ),

        scale=(

            STEP_RUN + 0.02,

            stair_height,

            STAIR_WIDTH

        ),

        color=color.rgb32(
            80,
            76,
            72
        ),

        collider="box"
    )


# ================================================================
# LANDING
# ================================================================

landing = Entity(

    model="cube",

    texture=concrete_texture,

    position=(

        8.80,

        HALF_HEIGHT / 2,

        -2.20

    ),

    scale=(

        1.15,

        HALF_HEIGHT,

        3.30

    ),

    color=color.rgb32(
        77,
        73,
        70
    ),

    collider="box"
)


# ================================================================
# UPPER FLIGHT
# ================================================================

upper_start_x = 8.55

upper_z = -3.45


for i in range(
    STEP_COUNT
):

    local_height = (

        (i + 1)
        *
        STEP_HEIGHT

    )


    Entity(

        model="cube",

        texture=concrete_texture,

        position=(

            upper_start_x
            -
            i * STEP_RUN,

            HALF_HEIGHT
            +
            local_height / 2,

            upper_z

        ),

        scale=(

            STEP_RUN + 0.02,

            local_height,

            STAIR_WIDTH

        ),

        color=color.rgb32(
            84,
            79,
            75
        ),

        collider="box"
    )


# ================================================================
# ÜST RESTORAN
#
# ARTIK ÇOK DAHA BÜYÜK.
#
# Merdiven alanı salonun içinde.
# ================================================================

REST_L = 0.0
REST_R = 16.5

REST_T = -13.0
REST_B = 2.0

REST_HEIGHT = 3.50


# ================================================================
# RESTORAN ZEMİNİ
#
# MERDİVEN BOŞLUĞUNU KAPATMIYORUZ.
#
# Merdiven boşluğu:
#
# X ~ 5.15 - 9.95
# Z ~ -4.65 - 0.15
#
# ================================================================


# Kuzey büyük bölüm

create_floor_level(

    REST_L,

    REST_R,

    REST_T,

    -4.65,

    FULL_HEIGHT,

    floor_color=color.rgb32(
        88,
        76,
        65
    ),

    texture=wood_texture
)


# Güney bölüm

create_floor_level(

    REST_L,

    REST_R,

    0.15,

    REST_B,

    FULL_HEIGHT,

    floor_color=color.rgb32(
        88,
        76,
        65
    ),

    texture=wood_texture
)


# Merdivenin sol tarafı

create_floor_level(

    REST_L,

    5.15,

    -4.65,

    0.15,

    FULL_HEIGHT,

    floor_color=color.rgb32(
        88,
        76,
        65
    ),

    texture=wood_texture
)


# Merdivenin sağ tarafı

create_floor_level(

    9.95,

    REST_R,

    -4.65,

    0.15,

    FULL_HEIGHT,

    floor_color=color.rgb32(
        88,
        76,
        65
    ),

    texture=wood_texture
)


# ================================================================
# ÜST MERDİVEN ÇIKIŞ LANDING
# ================================================================

upper_floor = Entity(

    model="cube",

    texture=wood_texture,

    position=(

        5.90,

        FULL_HEIGHT - 0.10,

        -3.30

    ),

    scale=(

        1.55,

        0.20,

        2.60

    ),

    color=color.rgb32(
        88,
        76,
        65
    ),

    collider="box"
)


# ================================================================
# RESTORAN DIŞ DUVARLARI
# ================================================================

wall_z(

    REST_L,

    REST_T,

    REST_B,

    base_y=FULL_HEIGHT,

    height=REST_HEIGHT,

    wall_color=RESTAURANT_WALL
)


wall_z(

    REST_R,

    REST_T,

    REST_B,

    base_y=FULL_HEIGHT,

    height=REST_HEIGHT,

    wall_color=RESTAURANT_WALL
)


# Güney duvar

wall_x(

    REST_L,

    REST_R,

    REST_B,

    base_y=FULL_HEIGHT,

    height=REST_HEIGHT,

    wall_color=RESTAURANT_WALL
)


# ================================================================
# RESTORAN ÖN KAPISI
# ================================================================

FRONT_DOOR_X = 8.30


wall_x_door(

    REST_L,

    REST_R,

    REST_T,

    FRONT_DOOR_X,

    base_y=FULL_HEIGHT,

    wall_height=REST_HEIGHT
)


restaurant_exit_door = SimpleDoor(

    position=(

        FRONT_DOOR_X,

        FULL_HEIGHT,

        REST_T

    ),

    axis="x",

    door_color=color.rgb32(
        74,
        58,
        46
    ),

    swing=90,

    name="RESTAURANT FRONT DOOR",

    final_lockable=True
)


# ================================================================
# RESTAURAN TAVANI
# ================================================================

Entity(

    model="cube",

    texture=concrete_texture,

    position=(

        (
            REST_L
            +
            REST_R
        ) / 2,

        FULL_HEIGHT
        +
        REST_HEIGHT
        +
        0.15,

        (
            REST_T
            +
            REST_B
        ) / 2

    ),

    scale=(

        REST_R - REST_L,

        0.30,

        REST_B - REST_T

    ),

    color=CEILING_COLOR,

    collider="box"
)


# ================================================================
# MERDİVEN KORKULUKLARI
#
# Merdiven salonun ortasında görünür.
# ================================================================

RAIL_HEIGHT = 1.0

RAIL_Y = (
    FULL_HEIGHT
    +
    RAIL_HEIGHT / 2
)


# Sol kenar

Entity(

    model="cube",

    position=(

        5.10,

        RAIL_Y,

        -1.95

    ),

    scale=(

        0.08,

        RAIL_HEIGHT,

        4.80

    ),

    color=DARK_METAL
)


# Sağ kenar

Entity(

    model="cube",

    position=(

        9.95,

        RAIL_Y,

        -2.25

    ),

    scale=(

        0.08,

        RAIL_HEIGHT,

        4.60

    ),

    color=DARK_METAL
)


# Üst / kuzey kenar

Entity(

    model="cube",

    position=(

        7.55,

        RAIL_Y,

        -4.62

    ),

    scale=(

        4.90,

        RAIL_HEIGHT,

        0.08

    ),

    color=DARK_METAL
)


# Güney kenarın sağ bölümü

Entity(

    model="cube",

    position=(

        8.30,

        RAIL_Y,

        0.12

    ),

    scale=(

        3.25,

        RAIL_HEIGHT,

        0.08

    ),

    color=DARK_METAL
)


# ================================================================
# TABLE SET
# ================================================================

def make_table_set(
    x,
    z
):

    # Orta ayak

    Entity(

        model="cube",

        position=(

            x,

            FULL_HEIGHT + 0.40,

            z

        ),

        scale=(

            0.16,

            0.80,

            0.16

        ),

        color=DARK_METAL
    )


    # Masa

    Entity(

        model="cube",

        texture=wood_texture,

        position=(

            x,

            FULL_HEIGHT + 0.83,

            z

        ),

        scale=(

            1.60,

            0.12,

            1.05

        ),

        color=color.rgb32(
            120,
            79,
            48
        ),

        collider="box"
    )


    chair_data = [

        (
            x - 1.05,
            z,
            90
        ),

        (
            x + 1.05,
            z,
            -90
        ),

        (
            x,
            z - 0.90,
            0
        ),

        (
            x,
            z + 0.90,
            180
        )

    ]


    for cx, cz, rotation_y in chair_data:

        chair = Entity(

            position=(

                cx,

                FULL_HEIGHT,

                cz

            ),

            rotation_y=rotation_y
        )


        Entity(

            parent=chair,

            model="cube",

            position=(

                0,

                0.45,

                0

            ),

            scale=(

                0.48,

                0.12,

                0.48

            ),

            color=color.rgb32(
                115,
                78,
                50
            ),

            collider="box"
        )


        Entity(

            parent=chair,

            model="cube",

            position=(

                0,

                0.82,

                0.20

            ),

            scale=(

                0.48,

                0.70,

                0.10

            ),

            color=color.rgb32(
                115,
                78,
                50
            )
        )


# ================================================================
# RESTORAN MASALARI
#
# Artık daha büyük restoran olduğu için 7 masa.
# ================================================================

make_table_set(
    2.7,
    -10.3
)


make_table_set(
    6.0,
    -10.3
)


make_table_set(
    10.3,
    -10.3
)


make_table_set(
    13.7,
    -10.3
)


make_table_set(
    2.7,
    -6.8
)


make_table_set(
    12.9,
    -6.7
)


make_table_set(
    13.0,
    -2.2
)


# ================================================================
# RESTORAN SERVİS BANKOSU
# ================================================================

Entity(

    model="cube",

    texture=wood_texture,

    position=(

        2.15,

        FULL_HEIGHT + 0.60,

        -2.25

    ),

    scale=(

        3.20,

        1.20,

        0.75

    ),

    color=color.rgb32(
        95,
        64,
        44
    ),

    collider="box"
)


# ================================================================
# RESTORAN IŞIKLARI
# ================================================================

for light_x in [

    2.5,

    6.0,

    10.0,

    14.0

]:

    for light_z in [

        -10.0,

        -6.5,

        -2.5

    ]:

        Entity(

            model="cube",

            position=(

                light_x,

                FULL_HEIGHT
                +
                REST_HEIGHT
                -
                0.12,

                light_z

            ),

            scale=(

                1.15,

                0.06,

                0.28

            ),

            color=color.rgb32(
                255,
                224,
                165
            )
        )


# ================================================================
# OUTSIDE
# ================================================================

OUTSIDE_Y = FULL_HEIGHT


# Genel zemin

create_floor_level(

    -3.0,

    20.0,

    -27.0,

    -13.0,

    OUTSIDE_Y,

    floor_color=color.rgb32(
        64,
        64,
        62
    )
)


# Restoran önü kaldırım

create_floor_level(

    0.0,

    17.0,

    -15.0,

    -13.0,

    OUTSIDE_Y + 0.03,

    floor_color=SIDEWALK_COLOR
)


# ================================================================
# ROAD
# ================================================================

create_floor_level(

    -1.0,

    18.0,

    -20.0,

    -15.0,

    OUTSIDE_Y + 0.04,

    floor_color=ROAD_COLOR,

    texture="white_cube"
)


# Karşı kaldırım

create_floor_level(

    0.0,

    17.0,

    -22.0,

    -20.0,

    OUTSIDE_Y + 0.05,

    floor_color=SIDEWALK_COLOR
)


# Yol çizgileri

for line_x in [

    1.2,

    4.2,

    7.2,

    10.2,

    13.2,

    16.2

]:

    Entity(

        model="cube",

        position=(

            line_x,

            OUTSIDE_Y + 0.08,

            -17.50

        ),

        scale=(

            1.55,

            0.02,

            0.10

        ),

        color=color.rgb32(
            225,
            214,
            160
        )
    )


# ================================================================
# DUMPSTER
#
# Yolun karşısı.
# ================================================================

dumpster_root = Entity(

    position=(

        8.3,

        OUTSIDE_Y,

        -21.15

    )
)


dumpster_body = Entity(

    parent=dumpster_root,

    model="cube",

    position=(

        0,

        0.62,

        0

    ),

    scale=(

        1.95,

        1.25,

        1.30

    ),

    color=DUMPSTER_COLOR,

    collider="box"
)


dumpster_body.interaction_type = (
    "dumpster"
)


# Kapak

Entity(

    parent=dumpster_root,

    model="cube",

    position=(

        0,

        1.37,

        0.12

    ),

    rotation_x=15,

    scale=(

        1.95,

        0.10,

        1.20

    ),

    color=color.rgb32(
        39,
        68,
        55
    )
)


# Dumpster içindeki diğer çöpler

for garbage_position in [

    (-0.55, 1.18, -0.15),

    (0.05, 1.25, -0.20),

    (0.55, 1.13, 0.12)

]:

    Entity(

        parent=dumpster_root,

        model="cube",

        position=garbage_position,

        rotation=(

            8,

            18,

            11

        ),

        scale=(

            0.52,

            0.42,

            0.48

        ),

        color=color.rgb32(
            22,
            23,
            23
        )
    )


# ================================================================
# BUILDINGS
# ================================================================

building_data = [

    (
        -1.5,
        -20.5,
        4.0,
        7.0,
        5.0
    ),

    (
        18.5,
        -20.5,
        5.0,
        8.0,
        5.5
    ),

    (
        2.5,
        -25.0,
        5.0,
        7.5,
        4.0
    ),

    (
        8.5,
        -25.0,
        5.0,
        9.0,
        4.0
    ),

    (
        15.0,
        -25.0,
        5.0,
        7.0,
        4.0
    )

]


for bx, bz, bw, bh, bd in building_data:

    Entity(

        model="cube",

        position=(

            bx,

            OUTSIDE_Y
            +
            bh / 2,

            bz

        ),

        scale=(

            bw,

            bh,

            bd

        ),

        color=color.rgb32(
            50,
            53,
            58
        ),

        collider="box"
    )


    # Pencereler

    for wy in [

        1.6,

        3.3,

        5.0

    ]:

        if wy < bh - 0.4:

            Entity(

                model="cube",

                position=(

                    bx,

                    OUTSIDE_Y + wy,

                    bz
                    +
                    bd / 2
                    +
                    0.02

                ),

                scale=(

                    bw * 0.55,

                    0.50,

                    0.04

                ),

                color=color.rgb32(
                    76,
                    92,
                    105
                )
            )


# ================================================================
# STREET LIGHTS
# ================================================================

for street_x in [

    2.0,

    8.5,

    15.0

]:

    Entity(

        model="cube",

        position=(

            street_x,

            OUTSIDE_Y + 1.75,

            -14.15

        ),

        scale=(

            0.10,

            3.50,

            0.10

        ),

        color=DARK_METAL
    )


    Entity(

        model="cube",

        position=(

            street_x,

            OUTSIDE_Y + 3.45,

            -14.15

        ),

        scale=(

            0.55,

            0.12,

            0.35

        ),

        color=color.rgb32(
            245,
            220,
            165
        )
    )


# ================================================================
# BASEMENT LIGHTS
# ================================================================

lamp_entities = []


lamp_positions = [

    (-9.4, 3.42, -6.2),

    (-9.2, 3.42, -0.5),

    (-3.0, 3.42, -6.2),

    (3.3, 3.42, -6.2),

    (-4.3, 3.42, -2.2),

    (-0.7, 3.42, -2.2),

    (3.0, 3.42, -2.2),

    (-2.7, 3.42, 2.8),

    (3.5, 3.42, 2.8)

]


for lamp_position in lamp_positions:

    lamp = Entity(

        model="cube",

        position=lamp_position,

        scale=(

            1.40,

            0.07,

            0.30

        ),

        color=color.rgb32(
            255,
            237,
            178
        )
    )


    lamp_entities.append(
        lamp
    )


# ================================================================
# PLAYER
# ================================================================

player = FirstPersonController(

    position=(

        -9.50,

        1,

        -5.80

    ),

    speed=0
)


player.gravity = 0

player.jump_height = 1.1


try:

    player.step_height = 0.30

except:

    pass


try:

    player.cursor.color = color.white

except:

    pass


mouse.locked = True


# ================================================================
# ARM
# ================================================================

arm_root = Entity(

    parent=camera,

    position=(

        0.42,

        -0.36,

        0.95

    ),

    rotation=(

        7,

        -18,

        -18

    ),

    enabled=False
)


Entity(

    parent=arm_root,

    model="cube",

    position=(

        0,

        0,

        0.24

    ),

    scale=(

        0.16,

        0.16,

        0.72

    ),

    color=SKIN_COLOR
)


Entity(

    parent=arm_root,

    model="cube",

    position=(

        -0.02,

        0,

        0.64

    ),

    scale=(

        0.20,

        0.18,

        0.24

    ),

    color=color.rgb32(
        215,
        170,
        130
    )
)


# ================================================================
# HELD MOP
# ================================================================

held_mop = Entity(

    parent=camera,

    position=(

        0.23,

        -0.28,

        1.02

    ),

    rotation=(

        10,

        -10,

        17

    ),

    enabled=False
)


Entity(

    parent=held_mop,

    model="cube",

    position=(

        0,

        0,

        0.38

    ),

    scale=(

        0.055,

        0.055,

        0.95

    ),

    color=color.rgb32(
        125,
        98,
        60
    )
)


Entity(

    parent=held_mop,

    model="cube",

    position=(

        0,

        -0.02,

        0.88

    ),

    scale=(

        0.52,

        0.12,

        0.28

    ),

    color=color.rgb32(
        210,
        208,
        190
    )
)


# ================================================================
# HELD KEY
# ================================================================

held_keys = Entity(

    parent=camera,

    position=(

        0.25,

        -0.17,

        1.05

    ),

    enabled=False
)


Entity(

    parent=held_keys,

    model="cube",

    position=(

        0,

        0,

        0

    ),

    scale=(

        0.55,

        0.08,

        0.05

    ),

    color=KEY_COLOR
)


# ================================================================
# HELD TRASH
# ================================================================

held_trash = Entity(

    parent=camera,

    position=(

        0.23,

        -0.25,

        0.95

    ),

    enabled=False
)


Entity(

    parent=held_trash,

    model="cube",

    position=(

        0,

        0,

        0.15

    ),

    scale=(

        0.58,

        0.70,

        0.55

    ),

    color=TRASH_COLOR
)


Entity(

    parent=held_trash,

    model="cube",

    position=(

        0,

        0.42,

        0.15

    ),

    rotation_z=45,

    scale=(

        0.20,

        0.22,

        0.18

    ),

    color=color.rgb32(
        12,
        12,
        12
    )
)


# ================================================================
# HELD ITEM
# ================================================================

def set_held_item(
    item_name
):

    global held_item


    held_item = item_name


    held_mop.enabled = False

    held_keys.enabled = False

    held_trash.enabled = False


    if item_name == "mop":

        held_mop.enabled = True


    elif item_name == "keys":

        held_keys.enabled = True


    elif item_name == "trash":

        held_trash.enabled = True


# ================================================================
# BLACKOUT
# ================================================================

blackout_overlay = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        2.2,

        1.3

    ),

    color=color.rgba32(
        0,
        0,
        0,
        135
    ),

    enabled=False,

    z=2
)


# ================================================================
# TASK UI
# ================================================================

task_panel = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        0.50,

        0.23

    ),

    position=(

        -0.59,

        0.38

    ),

    color=color.rgba32(
        0,
        0,
        0,
        125
    ),

    enabled=False,

    z=1
)


task_title = Text(

    parent=camera.ui,

    text="TASKS",

    position=(

        -0.815,

        0.455

    ),

    scale=1.15,

    color=color.white,

    enabled=False,

    z=0
)


task_text = Text(

    parent=camera.ui,

    text="",

    position=(

        -0.815,

        0.400

    ),

    scale=0.82,

    line_height=1.20,

    color=color.white,

    enabled=False,

    z=0
)


# ================================================================
# INTERACTION
# ================================================================

interaction_panel = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        0.42,

        0.06

    ),

    position=(

        0,

        -0.28

    ),

    color=color.rgba32(
        0,
        0,
        0,
        150
    ),

    enabled=False,

    z=1
)


interaction_text = Text(

    parent=camera.ui,

    text="",

    origin=(0, 0),

    position=(

        0,

        -0.29

    ),

    scale=0.82,

    color=color.white,

    enabled=False,

    z=0
)


# ================================================================
# COMPUTER UI
# ================================================================

computer_panel = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        0.62,

        0.48

    ),

    color=color.rgba32(
        5,
        12,
        8,
        235
    ),

    enabled=False,

    z=0
)


computer_title = Text(

    parent=camera.ui,

    text="SECURITY TERMINAL",

    origin=(0, 0),

    position=(

        0,

        0.16

    ),

    scale=1.5,

    color=color.rgb32(
        90,
        255,
        145
    ),

    enabled=False
)


computer_instruction = Text(

    parent=camera.ui,

    text="ENTER 4-DIGIT ACCESS CODE",

    origin=(0, 0),

    position=(

        0,

        0.08

    ),

    scale=0.95,

    color=color.white,

    enabled=False
)


computer_code_text = Text(

    parent=camera.ui,

    text="_ _ _ _",

    origin=(0, 0),

    position=(

        0,

        -0.02

    ),

    scale=1.8,

    color=color.rgb32(
        90,
        255,
        145
    ),

    enabled=False
)


computer_result = Text(

    parent=camera.ui,

    text="",

    origin=(0, 0),

    position=(

        0,

        -0.12

    ),

    scale=0.90,

    color=color.white,

    enabled=False
)


computer_help = Text(

    parent=camera.ui,

    text="ENTER = SUBMIT     ESC = EXIT",

    origin=(0, 0),

    position=(

        0,

        -0.20

    ),

    scale=0.68,

    color=color.gray,

    enabled=False
)


code_buffer = ""


# ================================================================
# CONTROLS
# ================================================================

controls_text = Text(

    parent=camera.ui,

    text=(

        "E = Interact   |   "
        "F = Mop / Switch   |   "
        "ESC = Mouse   |   "
        "F10 = Quit"

    ),

    origin=(0, 0),

    position=(

        0,

        -0.47

    ),

    scale=0.70,

    color=color.white,

    enabled=False
)


# ================================================================
# INTRO UI
# ================================================================

intro_top_bar = Entity(

    parent=camera.ui,

    model="quad",

    position=(

        0,

        0.47

    ),

    scale=(

        2,

        0.14

    ),

    color=color.black
)


intro_bottom_bar = Entity(

    parent=camera.ui,

    model="quad",

    position=(

        0,

        -0.47

    ),

    scale=(

        2,

        0.14

    ),

    color=color.black
)


intro_title = Text(

    parent=camera.ui,

    text="NIGHT SHIFT",

    origin=(0, 0),

    position=(

        0,

        -0.38

    ),

    scale=1.25,

    color=color.rgba32(
        255,
        255,
        255,
        185
    )
)


intro_fade = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        2.2,

        1.3

    ),

    color=color.rgba32(
        0,
        0,
        0,
        255
    ),

    z=-5
)


resume_text = Text(

    parent=camera.ui,

    text="CLICK TO CONTINUE",

    origin=(0, 0),

    scale=1.25,

    color=color.white,

    enabled=False
)


# ================================================================
# ENDING
# ================================================================

ending_background = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        2.2,

        1.3

    ),

    color=color.black,

    enabled=False,

    z=-10
)


ending_text = Text(

    parent=camera.ui,

    text="",

    origin=(0, 0),

    scale=1.8,

    color=color.white,

    enabled=False,

    z=-11
)


jumpscare_background = Entity(

    parent=camera.ui,

    model="quad",

    scale=(

        2.2,

        1.3

    ),

    color=color.black,

    enabled=False,

    z=-20
)


jumpscare_image = Entity(

    parent=camera.ui,

    model="quad",

    texture=jumpscare_texture,

    scale=(

        0.15,

        0.15

    ),

    enabled=False,

    z=-21
)


# ================================================================
# TASK UPDATE
# ================================================================

def update_tasks():

    if not has_mop:

        task_text.text = (

            "Pick up the mop\n"
            "Janitor Room"

        )

        return


    if not cleaning_done:

        task_text.text = (

            "Mop dirty floor near Kitchen\n"
            +
            str(clean_progress)
            +
            "/4 m² cleaned\n"
            "Press F"

        )

        return


    if (

        not power_on

        and

        not computer_unlocked

    ):

        task_text.text = (

            "Power failure\n"
            "Find code in Locker Room\n"
            "Use Security computer"

        )

        return


    if not has_keys:

        task_text.text = (

            "Find the key\n"
            "Kitchen countertop"

        )

        return


    if electrical_door.locked:

        task_text.text = (

            "Unlock Electrical Room\n"
            "Use the key"

        )

        return


    if not power_on:

        task_text.text = (

            "Restore electricity\n"
            "Look at switch and press F"

        )

        return


    if not has_trash:

        task_text.text = (

            "Take out the trash\n"
            "Trash bag is in Kitchen"

        )

        return


    if stairs_door.locked:

        task_text.text = (

            "Unlock stair door\n"
            "Use the key"

        )

        return


    if not restaurant_locked:

        task_text.text = (

            "Go upstairs through restaurant\n"
            "Leave through the front door\n"
            "Close it and press E to lock"

        )

        return


    if not trash_disposed:

        task_text.text = (

            "Cross the road\n"
            "Throw trash in dumpster"

        )

        return


    task_text.text = (
        "Shift complete."
    )


# ================================================================
# COMPUTER
# ================================================================

def open_computer():

    global computer_mode
    global game_active
    global code_buffer


    computer_mode = True

    game_active = False


    code_buffer = ""


    player.speed = 0

    player.gravity = 0


    mouse.locked = False


    computer_panel.enabled = True

    computer_title.enabled = True

    computer_instruction.enabled = True

    computer_code_text.enabled = True

    computer_result.enabled = True

    computer_help.enabled = True


    computer_code_text.text = (
        "_ _ _ _"
    )


    computer_result.text = ""


def close_computer():

    global computer_mode
    global game_active


    computer_mode = False

    game_active = True


    computer_panel.enabled = False

    computer_title.enabled = False

    computer_instruction.enabled = False

    computer_code_text.enabled = False

    computer_result.enabled = False

    computer_help.enabled = False


    mouse.locked = True


    player.speed = NORMAL_SPEED

    player.gravity = 1


def update_computer_code():

    result = ""


    for i in range(4):

        if i < len(
            code_buffer
        ):

            result += (
                code_buffer[i]
                +
                " "
            )

        else:

            result += "_ "


    computer_code_text.text = result


def submit_computer_code():

    global computer_unlocked


    if code_buffer == "1143":

        computer_unlocked = True


        computer_result.text = (

            "ACCESS GRANTED\n"
            "KEY IS ON THE KITCHEN COUNTERTOP"

        )


        computer_result.color = color.rgb32(
            80,
            255,
            130
        )


        world_key.enabled = True


        computer_screen.color = color.rgb32(
            40,
            150,
            80
        )


        update_tasks()


    else:

        computer_result.text = (
            "ACCESS DENIED"
        )


        computer_result.color = color.rgb32(
            255,
            70,
            70
        )


# ================================================================
# POWER
# ================================================================

def set_power(state):

    global power_on


    power_on = state


    if state:

        blackout_overlay.enabled = False


        for lamp in lamp_entities:

            lamp.color = color.rgb32(
                255,
                237,
                178
            )


        electric_led.color = color.rgb32(
            60,
            220,
            80
        )


        switch_lever.rotation_z = 28


    else:

        blackout_overlay.enabled = True


        for lamp in lamp_entities:

            lamp.color = color.rgb32(
                38,
                38,
                40
            )


        electric_led.color = color.rgb32(
            220,
            35,
            35
        )


        switch_lever.rotation_z = -28


    update_tasks()


# ================================================================
# MOP
# ================================================================

def pickup_mop():

    global has_mop


    if has_mop:

        return


    has_mop = True


    world_mop.enabled = False


    set_held_item(
        "mop"
    )


    show_notification(

        "MOP ACQUIRED\nDIRTY FLOOR IS NEAR KITCHEN"

    )


    update_tasks()


def player_near_clean_area():

    dx = player.x - (-2.25)

    dz = player.z - (-0.85)


    return (

        (
            dx * dx
            +
            dz * dz
        ) ** 0.5

        <= 2.0

    )


def reset_mop():

    held_mop.rotation_x = 10


def mop_floor():

    global clean_progress
    global cleaning_done


    if held_item != "mop":

        show_notification(
            "YOU NEED THE MOP"
        )

        return


    if cleaning_done:

        return


    if not player_near_clean_area():

        show_notification(
            "DIRTY FLOOR IS NEAR KITCHEN"
        )

        return


    held_mop.animate_rotation_x(

        58,

        duration=0.10
    )


    invoke(

        reset_mop,

        delay=0.12
    )


    clean_tiles[
        clean_progress
    ].enabled = False


    clean_progress += 1


    show_notification(

        str(clean_progress)
        +
        "/4 m² CLEANED",

        duration=1
    )


    if clean_progress >= clean_total:

        cleaning_done = True


        clean_marker.enabled = False


        set_held_item(
            None
        )


        show_notification(

            "CLEANING COMPLETE...\nPOWER FAILURE!",

            duration=3
        )


        set_power(
            False
        )


    update_tasks()


# ================================================================
# KEY
# ================================================================

def pickup_keys():

    global has_keys


    has_keys = True


    world_key.enabled = False


    set_held_item(
        "keys"
    )


    show_notification(
        "KEY ACQUIRED"
    )


    update_tasks()


# ================================================================
# SWITCH
# ================================================================

def use_power_switch():

    global electrical_switched_on


    if power_on:

        show_notification(
            "POWER IS ALREADY ON"
        )

        return


    electrical_switched_on = True


    set_power(
        True
    )


    show_notification(
        "POWER RESTORED"
    )


# ================================================================
# TRASH
# ================================================================

def pickup_trash():

    global has_trash


    # ------------------------------------------------------------
    # Story sırası gelmeden çöp görünür ama alınamaz.
    # ------------------------------------------------------------

    if not cleaning_done:

        show_notification(
            "FINISH CLEANING FIRST"
        )

        return


    if not power_on:

        show_notification(
            "RESTORE THE POWER FIRST"
        )

        return


    if has_trash:

        return


    has_trash = True


    world_trash.enabled = False


    set_held_item(
        "trash"
    )


    show_notification(

        "TRASH BAG ACQUIRED\nTAKE IT OUTSIDE",

        duration=2.5
    )


    update_tasks()


# ================================================================
# DUMPSTER
# ================================================================

def dispose_trash():

    global has_trash
    global trash_disposed


    if not restaurant_locked:

        show_notification(
            "LOCK THE RESTAURANT FIRST"
        )

        return


    if not has_trash:

        show_notification(
            "YOU DON'T HAVE THE TRASH"
        )

        return


    has_trash = False

    trash_disposed = True


    set_held_item(
        None
    )


    update_tasks()


    show_notification(
        "TRASH DISPOSED"
    )


    invoke(

        begin_ending,

        delay=1.2
    )


# ================================================================
# ENDING
# ================================================================

def begin_ending():

    global ending_started
    global game_active


    ending_started = True

    game_active = False


    player.speed = 0

    player.gravity = 0


    arm_root.enabled = False


    task_panel.enabled = False

    task_title.enabled = False

    task_text.enabled = False


    controls_text.enabled = False


    ending_background.enabled = True

    ending_text.enabled = True


    ending_text.text = (
        "YOU'VE FINISHED YOUR SHIFT..."
    )


    invoke(

        show_or_have_you,

        delay=2.4
    )


def show_or_have_you():

    ending_text.text = (
        "OR HAVE YOU?"
    )


    invoke(

        play_jumpscare,

        delay=1.6
    )


def play_jumpscare():

    ending_background.enabled = False

    ending_text.enabled = False


    jumpscare_background.enabled = True

    jumpscare_image.enabled = True


    jumpscare_image.scale = (
        0.12,
        0.12
    )


    jumpscare_image.animate_scale(

        (
            1.45,
            1.45
        ),

        duration=0.10
    )


# ================================================================
# INTRO
# ================================================================

def start_intro():

    global intro_playing
    global game_active


    intro_playing = True

    game_active = False


    player.speed = 0

    player.gravity = 0


    arm_root.enabled = False


    mouse.locked = True


    # Introda geçilecek kapılar açık.

    locker_door.pivot.rotation_y = (
        locker_door.swing
    )

    locker_door.is_open = True


    janitor_door.pivot.rotation_y = (
        janitor_door.swing
    )

    janitor_door.is_open = True


    camera.parent = scene


    camera.position = (

        2.7,

        1.70,

        -2.15

    )


    camera.rotation = (

        0,

        -90,

        0

    )


    camera.fov = 75


    intro_fade.animate_color(

        color.rgba32(
            0,
            0,
            0,
            0
        ),

        duration=1.2
    )


    invoke(

        intro_part_1,

        delay=0.8
    )


def intro_part_1():

    camera.animate_position(

        (
            -4.40,
            1.70,
            -2.15
        ),

        duration=2.5,

        curve=curve.in_out_quad
    )


    invoke(

        intro_part_2,

        delay=2.6
    )


def intro_part_2():

    camera.animate_rotation_y(

        180,

        duration=0.45
    )


    camera.animate_position(

        (
            -4.45,
            1.70,
            -5.80
        ),

        duration=1.7,

        curve=curve.in_out_quad
    )


    invoke(

        intro_part_3,

        delay=1.75
    )


def intro_part_3():

    camera.animate_rotation_y(

        -90,

        duration=0.45
    )


    camera.animate_position(

        (
            -8.75,
            1.70,
            -6.25
        ),

        duration=1.7,

        curve=curve.in_out_quad
    )


    invoke(

        finish_intro,

        delay=1.8
    )


def finish_intro():

    intro_fade.animate_color(

        color.rgba32(
            0,
            0,
            0,
            255
        ),

        duration=0.30
    )


    invoke(

        activate_player,

        delay=0.32
    )


def activate_player():

    global intro_playing
    global game_active


    try:

        camera.parent = player.camera_pivot

    except:

        camera.parent = player


    camera.position = (
        0,
        0,
        0
    )


    camera.rotation = (
        0,
        0,
        0
    )


    camera.fov = 90


    locker_door.pivot.rotation_y = 0

    locker_door.is_open = False


    janitor_door.pivot.rotation_y = 0

    janitor_door.is_open = False


    arm_root.enabled = True


    task_panel.enabled = True

    task_title.enabled = True

    task_text.enabled = True

    controls_text.enabled = True


    intro_top_bar.enabled = False

    intro_bottom_bar.enabled = False

    intro_title.enabled = False


    intro_playing = False

    game_active = True


    player.speed = NORMAL_SPEED

    player.gravity = 1


    update_tasks()


    intro_fade.animate_color(

        color.rgba32(
            0,
            0,
            0,
            0
        ),

        duration=0.45
    )


    invoke(

        setattr,

        intro_fade,

        "enabled",

        False,

        delay=0.5
    )


# ================================================================
# UPDATE
# ================================================================

def update():

    global current_interactable
    global current_door


    current_interactable = None

    current_door = None


    interaction_panel.enabled = False

    interaction_text.enabled = False


    if intro_playing:

        return


    if ending_started:

        return


    if not game_active:

        return


    hit = raycast(

        origin=camera.world_position,

        direction=camera.forward,

        distance=2.70,

        ignore=[
            player
        ]
    )


    if not hit.hit:

        return


    entity = hit.entity


    # ============================================================
    # DOOR
    # ============================================================

    if hasattr(
        entity,
        "simple_door"
    ):

        current_door = (
            entity.simple_door
        )


        interaction_panel.enabled = True

        interaction_text.enabled = True


        # Restaurant final door

        if current_door.final_lockable:

            if current_door.final_locked:

                interaction_text.text = (
                    "[LOCKED] RESTAURANT SECURED"
                )

                return


            outside = (

                player.z

                <

                current_door.root.z
                -
                0.35

            )


            if (

                outside

                and

                not current_door.is_open

            ):

                interaction_text.text = (
                    "[E] LOCK RESTAURANT"
                )

                return


        if current_door.locked:

            if has_keys:

                if (

                    current_door.requires_power

                    and

                    not power_on

                ):

                    interaction_text.text = (
                        "[LOCKED] RESTORE POWER FIRST"
                    )

                else:

                    interaction_text.text = (
                        "[E] UNLOCK WITH KEY"
                    )


            else:

                interaction_text.text = (
                    "[LOCKED] KEY REQUIRED"
                )


        elif current_door.is_open:

            interaction_text.text = (
                "[E] CLOSE DOOR"
            )


        else:

            interaction_text.text = (
                "[E] OPEN DOOR"
            )


        return


    # ============================================================
    # OTHER
    # ============================================================

    if hasattr(
        entity,
        "interaction_type"
    ):

        current_interactable = entity


        interaction_panel.enabled = True

        interaction_text.enabled = True


        interaction_type = (
            entity.interaction_type
        )


        if interaction_type == "mop":

            interaction_text.text = (
                "[E] PICK UP MOP"
            )


        elif interaction_type == "computer":

            interaction_text.text = (
                "[E] USE COMPUTER"
            )


        elif interaction_type == "note":

            interaction_text.text = (
                "[E] READ POST-IT"
            )


        elif interaction_type == "keys":

            interaction_text.text = (
                "[E] PICK UP KEY"
            )


        elif interaction_type == "power_switch":

            interaction_text.text = (
                "[F] USE POWER SWITCH"
            )


        elif interaction_type == "trash":

            if not cleaning_done:

                interaction_text.text = (
                    "[TRASH] FINISH CLEANING FIRST"
                )

            elif not power_on:

                interaction_text.text = (
                    "[TRASH] RESTORE POWER FIRST"
                )

            else:

                interaction_text.text = (
                    "[E] PICK UP TRASH"
                )


        elif interaction_type == "dumpster":

            if not restaurant_locked:

                interaction_text.text = (
                    "[E] LOCK RESTAURANT FIRST"
                )

            elif has_trash:

                interaction_text.text = (
                    "[E] THROW TRASH"
                )

            else:

                interaction_text.text = (
                    "YOU NEED THE TRASH"
                )


# ================================================================
# INPUT
# ================================================================

def input(key):

    global game_active
    global code_buffer


    if intro_playing:

        if key == "f10":

            application.quit()

        return


    if ending_started:

        if key == "f10":

            application.quit()

        return


    # ============================================================
    # COMPUTER MODE
    # ============================================================

    if computer_mode:

        if (

            len(key) == 1

            and

            key in "0123456789"

        ):

            if len(
                code_buffer
            ) < 4:

                code_buffer += key


                update_computer_code()


            return


        if key == "backspace":

            code_buffer = (
                code_buffer[:-1]
            )


            update_computer_code()

            return


        if key == "enter":

            submit_computer_code()

            return


        if key == "escape":

            close_computer()

            return


        return


    # ============================================================
    # RESUME
    # ============================================================

    if key == "left mouse down":

        if not game_active:

            game_active = True


            player.speed = NORMAL_SPEED

            player.gravity = 1


            mouse.locked = True


            resume_text.enabled = False


    # ============================================================
    # ESC
    # ============================================================

    if key == "escape":

        game_active = False


        player.speed = 0

        player.gravity = 0


        mouse.locked = False


        resume_text.enabled = True


    # ============================================================
    # F
    # ============================================================

    if key == "f":

        if current_interactable is not None:

            if (

                hasattr(
                    current_interactable,
                    "interaction_type"
                )

                and

                current_interactable.interaction_type
                ==
                "power_switch"

            ):

                use_power_switch()

                return


        mop_floor()

        return


    # ============================================================
    # E
    # ============================================================

    if key == "e":

        if current_door is not None:

            current_door.interact()

            return


        if current_interactable is None:

            return


        interaction_type = (
            current_interactable.interaction_type
        )


        if interaction_type == "mop":

            pickup_mop()

            return


        if interaction_type == "computer":

            open_computer()

            return


        if interaction_type == "note":

            show_notification(

                "POST-IT CODE: 1143",

                duration=3
            )

            return


        if interaction_type == "keys":

            pickup_keys()

            return


        if interaction_type == "power_switch":

            show_notification(

                "PRESS F TO USE SWITCH"

            )

            return


        if interaction_type == "trash":

            pickup_trash()

            return


        if interaction_type == "dumpster":

            dispose_trash()

            return


    # ============================================================
    # F10
    # ============================================================

    if key == "f10":

        application.quit()


# ================================================================
# START INTRO
# ================================================================

invoke(

    start_intro,

    delay=0.35
)


# ================================================================
# RUN
# ================================================================

app.run()