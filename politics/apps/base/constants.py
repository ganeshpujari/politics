from django.utils.translation import ugettext_lazy as _
DEFAULT_NATIONALITY_INDIAN='indian'
#______________Address model constants_________________________________

ADDRESS_TYPE_CHOICE_PLOT = "PLOT"
ADDRESS_TYPE_CHOICE_HOME = "HOME"
ADDRESS_TYPE_CHOICE_WORK = "WORK"
ADDRESS_TYPE_CHOICE_OTHER = "OTHER"

ADDRESS_TYPE_TUPLE_PLOT = (ADDRESS_TYPE_CHOICE_PLOT, _("Plot"))
ADDRESS_TYPE_TUPLE_HOME = (ADDRESS_TYPE_CHOICE_HOME, _("Home"))
ADDRESS_TYPE_TUPLE_WORK = (ADDRESS_TYPE_CHOICE_WORK, _("Work"))
ADDRESS_TYPE_TUPLE_OTHER = (ADDRESS_TYPE_CHOICE_OTHER, _("Other"))


ADDRESS_TYPE_CHOICE = (
    ADDRESS_TYPE_TUPLE_PLOT,
    ADDRESS_TYPE_TUPLE_HOME,
    ADDRESS_TYPE_TUPLE_WORK,
    ADDRESS_TYPE_TUPLE_OTHER
)

#_____________Education_MODELS------------------------

EDUCATION_CATEGORY_SSC='ssc'
EDUCATION_CATEGORY_HSC='hsc'
EDUCATION_CATEGORY_DIPLOMA='diploma'
EDUCATION_CATEGORY_GRADUATION='graduation'
EDUCATION_CATEGORY_POST_GRADUATION='post_graduation'
EDUCATION_CATEGORY_OTHER='other'

EDUCATION_CATEGORY_CHOICES=((EDUCATION_CATEGORY_SSC, EDUCATION_CATEGORY_SSC),
                            (EDUCATION_CATEGORY_HSC, EDUCATION_CATEGORY_HSC),
                            (EDUCATION_CATEGORY_DIPLOMA,EDUCATION_CATEGORY_DIPLOMA),
                            (EDUCATION_CATEGORY_GRADUATION,EDUCATION_CATEGORY_GRADUATION),
                            (EDUCATION_CATEGORY_OTHER, EDUCATION_CATEGORY_OTHER))

FAIL='fail'
PASS='pass'
FIRST_CLASS='first_class'
SECOND_CLASS='second_class'
HIGHER_SECOND_CLASS='higher_second_class'
PURSUING='pursuing'


EDUCATION_GRADE_CHOICES=((FAIL, FAIL),
                        (PASS, PASS),
                        (FIRST_CLASS,FIRST_CLASS),
                        (SECOND_CLASS,SECOND_CLASS),
                        (HIGHER_SECOND_CLASS, HIGHER_SECOND_CLASS),
                        (PURSUING, PURSUING))

# __________Work model type----------------------

WORK_TYPE_POLITICAL='political'
WORK_TYPE_SOCIAL='social'
FOUNDATION='foundations'
NGO='ngo'

POLITICIAL_WORK_TYPE_CHOICES=((WORK_TYPE_POLITICAL, WORK_TYPE_POLITICAL),
                        (WORK_TYPE_SOCIAL, WORK_TYPE_SOCIAL),
                        (FOUNDATION, FOUNDATION),
                        (NGO, NGO),
                        )

#__________Family relation model_____________

RELATION_TYPE_FATHER='father'
RELATION_TYPE_MOTHER='mother'
RELATION_TYPE_SON='son'
RELATION_TYPE_DAUGHTER='daughter'

RELATION_TYPE_CHOICES=((RELATION_TYPE_FATHER, RELATION_TYPE_FATHER),
                        (RELATION_TYPE_MOTHER, RELATION_TYPE_MOTHER),
                        (RELATION_TYPE_SON, RELATION_TYPE_SON),
                        (RELATION_TYPE_DAUGHTER, RELATION_TYPE_DAUGHTER),
                        )




#__________Assets type model_____________
CASH='cash'
BANK_BALANCE='bank_balance'
INVESTMENT='investment'
LAND='land'
FLATS='flats'


ASSETS_TYPE_CHOICES=((CASH, CASH),
                        (BANK_BALANCE,BANK_BALANCE ),
                        (INVESTMENT,INVESTMENT ),
                        (LAND,LAND ),
                        (FLATS,FLATS ),
                        )

#________________Media type model_____________

PUBLICATION="Publication"
GALLERY="gallery"

MEDIA_TYPE_CHOICES=((PUBLICATION, PUBLICATION),
                        (GALLERY,GALLERY ),

                        )

#___________OTP TYPE_______________
SIGNUP='signup'