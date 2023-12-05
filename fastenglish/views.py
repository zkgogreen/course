from django.shortcuts import redirect
from owner.models import LevelAkun, Level, Kategori, Master, Setting
from teacher.models import Kelas, Bab, Pelajaran, Questions, Room, Schadule
from user.models import Users, UserBab, UserCourse, UserLatihan, UserLesson, UserMeeting, UserSchadule
from django.contrib.auth.models import User as user_root

import datetime
x = datetime.datetime.now()

def home(request):
    return redirect("user:index")

def begin(request):
    # level akun
    levelakun1  = LevelAkun.objects.create(foto="free.jpg",name='free', keterangan='belajar bahasa inggris tidak butuh biaya',  nyawa=5, biaya=0, discount=0,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek"),
    levelakun2  = LevelAkun.objects.create(foto="private.jpg",name='membersip', keterangan='belajar bahasa inggris dengan intensif',  nyawa=100, biaya=80000,discount=80000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    levelakun3  = LevelAkun.objects.create(foto="regular.jpg",name='Premium', keterangan='belajar bahasa inggris tanpa batasan', nyawa=100, biaya=120000,discount=120000,promo=0,materi="GRAMMAR FOR SPEAKING, PRONUNCIATION, VOCABULARY, SPEAKING PRACTICE", bonus="Garansi mengulang, Free 60x Written Class, Free 10x Pronunciation Class, Gratis konsultasi langsung dengan tutor", ketentuan="Microphone wajib aktif ketika sesi praktek, Biaya tidak hangus jika tidak hadir, Bebas pilih jadwal atau merubah jadwal, Dilarang keras membahas isu politik atau SARA ketika praktek")
    
    #level
    level1      = Level.objects.create(name="Beginner", keterangan="kemampuan bahasa Inggris yang masih sangat dasar.")
    level2      = Level.objects.create(name="Elementary", keterangan="dapat berkomunikasi dengan bahasa Inggris, tetapi pembahasan hanya mencakup hal-hal tertentu yang telah dikuasai.")
    level3      = Level.objects.create(name="Intermediate", keterangan="berbahasa Inggris secara pasif dan aktif dengan topik yang lebih variatif.")
    level4      = Level.objects.create(name="Advanced", keterangan="menggunakan bahasa Inggris untuk kepentingan akademis dan profesional.")
    level5      = Level.objects.create(name="Expert", keterangan="setara dengan native speaker (penutur asli)")

    #kategori
    kategori1   = Kategori.objects.create(name="Speaking", keterangan="Kemampuan Berbicara ")
    kategori2   = Kategori.objects.create(name="Reading", keterangan="Kemampuan Membaca")
    kategori3   = Kategori.objects.create(name="Listening", keterangan="Keterampilan Menyimak")
    kategori4   = Kategori.objects.create(name="Writing", keterangan="Kemampuan Menulis")

    #master
    master1     = Master.objects.create(name="TOEFL", keterangan="Test of English as Foregn Language")
    master2     = Master.objects.create(name="Public Speaking", keterangan="Keterampilan berbicara dengan banyak orang")

    #kelas
    kelas1      = Kelas.objects.create(kelas="Kelas pertama", bahasa=1, slug="SpeakingDasar", photo="kelas/bannerexample2.png", kategori=kategori1, level=level1,
                                              keterangan="keterangan", rangkuman="rangkuman", urutan=1)
    
    k1b1        = Bab.objects.create(kelas=kelas1, bab="Bab 1", urutan=1, rangkuman="ini adalah rangkuman")
    k1b1p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b1, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p1q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p1q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p1q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b1p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b1, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p2q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p2q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p2q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b1, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p3q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p3q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p3q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b1, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p4q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p4q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p4q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b1, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p5q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p5q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p5q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    
    k1b2        = Bab.objects.create(kelas=kelas1, bab="Bab 2", urutan=2, rangkuman="ini adalah rangkuman")
    
    k1b2p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b2, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p1q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p1q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p1q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b2p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b2, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p2q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p2q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p2q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b2, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p3q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p3q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p3q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b2, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p4q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p4q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p4q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b2, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p5q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p5q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p5q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
        
    k1b3        = Bab.objects.create(kelas=kelas1, bab="Bab 3", urutan=3, rangkuman="ini adalah rangkuman")
    
    k1b3p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b3, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p1q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p1q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p1q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b3p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b3, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p2q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p2q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p2q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b3, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p3q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p3q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p3q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b3, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p4q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p4q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p4q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b3, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p5q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p5q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p5q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    #kelas 2
    kelas2      = Kelas.objects.create(kelas="Speaking Intermediate", bahasa=1, slug="SpeakingIntermediate", photo="kelas/bannerexample1.png", kategori=kategori1, level=level3,
                                              keterangan="keterangan", rangkuman="rangkuman", urutan=2)
    
    k2b1        = Bab.objects.create(kelas=kelas2, bab="Bab 1", urutan=1, rangkuman="ini adalah rangkuman")
    k2b1p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b1, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p1q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p1q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p1q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b1p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b1, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p2q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p2q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p2q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b1, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p3q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p3q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p3q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b1, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p4q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p4q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p4q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b1, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p5q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p5q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p5q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    
    k2b2        = Bab.objects.create(kelas=kelas2, bab="Bab 2", urutan=2, rangkuman="ini adalah rangkuman")
    
    k2b2p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b2, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p1q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p1q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p1q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b2p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b2, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p2q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p2q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p2q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b2, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p3q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p3q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p3q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b2, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p4q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p4q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p4q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b2, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p5q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p5q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p5q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
        
    k2b3        = Bab.objects.create(kelas=kelas2, bab="Bab 3", urutan=3, rangkuman="ini adalah rangkuman")
    
    k2b3p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b3, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p1q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p1q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p1q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b3p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b3, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p2q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p2q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p2q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b3, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p3q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p3q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p3q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b3, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p4q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p4q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p4q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b3, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p5q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p5q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p5q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    #Landing
    if not Setting.objects.all().exists():
        Setting.objects.create(title="Belajar bahasa inggris", sub="belajar bahasa inggris")
    
    user_1 = user_root.objects.create_user(username="user_1", email="user_1@localhost", first_name="user", last_name="name", password="user1234")
    user_2 = user_root.objects.create_user(username="user_2", email="user_2@localhost", first_name="user2", last_name="name", password="user1234")
    user_3 = user_root.objects.create_user(username="user_3", email="user_3@localhost", first_name="user3", last_name="name", password="user1234")
    user_4 = user_root.objects.create_user(username="user_4", email="user_4@localhost", first_name="user4", last_name="name", password="user1234")
    user_5 = user_root.objects.create_user(username="user_5", email="user_5@localhost", first_name="user5", last_name="name", password="user1234")
    
    mentor_1 = user_root.objects.create_user(username="mentor_1", email="mentor_1@localhost", first_name="mentor", last_name="name", password="mentor1234")
    mentor_2 = user_root.objects.create_user(username="mentor_2", email="mentor_2@localhost", first_name="mentor2", last_name="name", password="mentor1234")
    mentor_3 = user_root.objects.create_user(username="mentor_3", email="mentor_3@localhost", first_name="mentor3", last_name="name", password="mentor1234")
    mentor_4 = user_root.objects.create_user(username="mentor_4", email="mentor_4@localhost", first_name="mentor4", last_name="name", password="mentor1234")
    mentor_5 = user_root.objects.create_user(username="mentor_5", email="mentor_5@localhost", first_name="mentor5", last_name="name", password="mentor1234")
    
    myuser = Users.objects.create(user=user_1)
    myuser2 = Users.objects.create(user=user_2)
    myuser3 = Users.objects.create(user=user_3)
    myuser4 = Users.objects.create(user=user_4)
    myuser5 = Users.objects.create(user=user_5)

    mymentor1 = Users.objects.create(user=mentor_1)
    mymentor2 = Users.objects.create(user=mentor_2)
    mymentor3 = Users.objects.create(user=mentor_3)
    mymentor4 = Users.objects.create(user=mentor_4)
    mymentor5 = Users.objects.create(user=mentor_5)

    usermeeting_1 = UserMeeting.objects.create(mentor= mentor_1,user=user_1, accountlevel=levelakun3, end=x.month+levelakun3.duration, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_2 = UserMeeting.objects.create(mentor= mentor_2,user=user_2, accountlevel=levelakun2, end=x.month+levelakun2.duration, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_3 = UserMeeting.objects.create(mentor= mentor_3,user=user_3, accountlevel=levelakun3, end=x.month+levelakun3.duration, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_4 = UserMeeting.objects.create(mentor= mentor_4,user=user_4, accountlevel=levelakun2, end=x.month+levelakun2.duration, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_5 = UserMeeting.objects.create(mentor= mentor_5,user=user_5, accountlevel=levelakun3, end=x.month+levelakun3.duration, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_6 = UserMeeting.objects.create(mentor= mentor_1,user=user_1, accountlevel=levelakun2, end=x.month+levelakun2.duration, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_7 = UserMeeting.objects.create(mentor= mentor_2,user=user_2, accountlevel=levelakun3, end=x.month+levelakun3.duration, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_8 = UserMeeting.objects.create(mentor= mentor_3,user=user_3, accountlevel=levelakun2, end=x.month+levelakun2.duration, meetremain=levelakun3.meeting, purchased=True)
    usermeeting_9 = UserMeeting.objects.create(mentor= mentor_4,user=user_4, accountlevel=levelakun3, end=x.month+levelakun3.duration, meetremain=levelakun2.meeting, purchased=True)
    usermeeting_10 = UserMeeting.objects.create(mentor= mentor_5,user=user_5, accountlevel=levelakun2, end=x.month+levelakun2.duration, meetremain=levelakun3.meeting, purchased=True)

    room_1 = Room.objects.create(mentor=mentor_1, bahasa=1, time=1, mulai=1, level=levelakun2)
    room_2 = Room.objects.create(mentor=mentor_2, bahasa=1, time=1, mulai=1, level=levelakun3)
    room_3 = Room.objects.create(mentor=mentor_3, bahasa=1, time=1, mulai=1, level=levelakun2)
    room_4 = Room.objects.create(mentor=mentor_4, bahasa=1, time=1, mulai=1, level=levelakun3)
    room_5 = Room.objects.create(mentor=mentor_5, bahasa=1, time=1, mulai=1, level=levelakun2)

    room_1_sch_1 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_2 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_3 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_4 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)
    room_1_sch_5 = Schadule.objects.create(room=room_1, mentor=mentor_1, level=levelakun2, tanggal=x)

    room_2_sch_1 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_2 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_3 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_4 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)
    room_2_sch_5 = Schadule.objects.create(room=room_2, mentor=mentor_2, level=levelakun2, tanggal=x)

    room_3_sch_1 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_2 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_3 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_4 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)
    room_3_sch_5 = Schadule.objects.create(room=room_3, mentor=mentor_3, level=levelakun2, tanggal=x)

    room_4_sch_1 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_2 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_3 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_4 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)
    room_4_sch_5 = Schadule.objects.create(room=room_4, mentor=mentor_4, level=levelakun3, tanggal=x)

    room_5_sch_1 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_2 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_3 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_4 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    room_5_sch_5 = Schadule.objects.create(room=room_5, mentor=mentor_5, level=levelakun3, tanggal=x)
    # room_1
    user_1_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_1, tanggal=x)
    user_1_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_1, tanggal=x)
    user_1_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_1, tanggal=x)
    user_1_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_1, tanggal=x)
    user_1_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_1, tanggal=x)
    
    user_2_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_2, tanggal=x)
    user_2_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_2, tanggal=x)
    user_2_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_2, tanggal=x)
    user_2_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_2, tanggal=x)
    user_2_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_2, tanggal=x)
    
    user_3_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_3, tanggal=x)
    user_3_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_3, tanggal=x)
    user_3_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_3, tanggal=x)
    user_3_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_3, tanggal=x)
    user_3_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_3, tanggal=x)
    
    user_4_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_4, tanggal=x)
    user_4_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_4, tanggal=x)
    user_4_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_4, tanggal=x)
    user_4_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_4, tanggal=x)
    user_4_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_4, tanggal=x)
    
    user_5_room_1_sch_1 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_1, user=user_5, tanggal=x)
    user_5_room_1_sch_2 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_2, user=user_5, tanggal=x)
    user_5_room_1_sch_3 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_3, user=user_5, tanggal=x)
    user_5_room_1_sch_4 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_4, user=user_5, tanggal=x)
    user_5_room_1_sch_5 = UserSchadule.objects.create(room=room_1, schadule=room_1_sch_5, user=user_5, tanggal=x)

    # room_2
    user_1_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_1, tanggal=x)
    user_1_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_1, tanggal=x)
    user_1_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_1, tanggal=x)
    user_1_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_1, tanggal=x)
    user_1_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_1, tanggal=x)
    
    user_2_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_2, tanggal=x)
    user_2_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_2, tanggal=x)
    user_2_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_2, tanggal=x)
    user_2_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_2, tanggal=x)
    user_2_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_2, tanggal=x)
    
    user_3_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_3, tanggal=x)
    user_3_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_3, tanggal=x)
    user_3_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_3, tanggal=x)
    user_3_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_3, tanggal=x)
    user_3_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_3, tanggal=x)
    
    user_4_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_4, tanggal=x)
    user_4_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_4, tanggal=x)
    user_4_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_4, tanggal=x)
    user_4_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_4, tanggal=x)
    user_4_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_4, tanggal=x)
    
    user_5_room_2_sch_1 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_1, user=user_5, tanggal=x)
    user_5_room_2_sch_2 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_2, user=user_5, tanggal=x)
    user_5_room_2_sch_3 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_3, user=user_5, tanggal=x)
    user_5_room_2_sch_4 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_4, user=user_5, tanggal=x)
    user_5_room_2_sch_5 = UserSchadule.objects.create(room=room_2, schadule=room_2_sch_5, user=user_5, tanggal=x)

    
    # room_3
    user_1_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_1, tanggal=x)
    user_1_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_1, tanggal=x)
    user_1_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_1, tanggal=x)
    user_1_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_1, tanggal=x)
    user_1_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_1, tanggal=x)
    
    user_2_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_2, tanggal=x)
    user_2_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_2, tanggal=x)
    user_2_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_2, tanggal=x)
    user_2_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_2, tanggal=x)
    user_2_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_2, tanggal=x)
    
    user_3_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_3, tanggal=x)
    user_3_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_3, tanggal=x)
    user_3_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_3, tanggal=x)
    user_3_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_3, tanggal=x)
    user_3_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_3, tanggal=x)
    
    user_4_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_4, tanggal=x)
    user_4_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_4, tanggal=x)
    user_4_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_4, tanggal=x)
    user_4_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_4, tanggal=x)
    user_4_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_4, tanggal=x)
    
    user_5_room_3_sch_1 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_1, user=user_5, tanggal=x)
    user_5_room_3_sch_2 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_2, user=user_5, tanggal=x)
    user_5_room_3_sch_3 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_3, user=user_5, tanggal=x)
    user_5_room_3_sch_4 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_4, user=user_5, tanggal=x)
    user_5_room_3_sch_5 = UserSchadule.objects.create(room=room_3, schadule=room_3_sch_5, user=user_5, tanggal=x)
    
    # room_4
    user_1_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_1, tanggal=x)
    user_1_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_1, tanggal=x)
    user_1_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_1, tanggal=x)
    user_1_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_1, tanggal=x)
    user_1_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_1, tanggal=x)
    
    user_2_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_2, tanggal=x)
    user_2_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_2, tanggal=x)
    user_2_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_2, tanggal=x)
    user_2_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_2, tanggal=x)
    user_2_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_2, tanggal=x)
    
    user_3_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_3, tanggal=x)
    user_3_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_3, tanggal=x)
    user_3_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_3, tanggal=x)
    user_3_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_3, tanggal=x)
    user_3_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_3, tanggal=x)
    
    user_4_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_4, tanggal=x)
    user_4_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_4, tanggal=x)
    user_4_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_4, tanggal=x)
    user_4_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_4, tanggal=x)
    user_4_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_4, tanggal=x)
    
    user_5_room_4_sch_1 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_1, user=user_5, tanggal=x)
    user_5_room_4_sch_2 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_2, user=user_5, tanggal=x)
    user_5_room_4_sch_3 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_3, user=user_5, tanggal=x)
    user_5_room_4_sch_4 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_4, user=user_5, tanggal=x)
    user_5_room_4_sch_5 = UserSchadule.objects.create(room=room_4, schadule=room_4_sch_5, user=user_5, tanggal=x)
    
    # room_5
    user_1_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_1, tanggal=x)
    user_1_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_1, tanggal=x)
    user_1_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_1, tanggal=x)
    user_1_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_1, tanggal=x)
    user_1_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_1, tanggal=x)
    
    user_2_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_2, tanggal=x)
    user_2_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_2, tanggal=x)
    user_2_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_2, tanggal=x)
    user_2_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_2, tanggal=x)
    user_2_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_2, tanggal=x)
    
    user_3_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_3, tanggal=x)
    user_3_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_3, tanggal=x)
    user_3_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_3, tanggal=x)
    user_3_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_3, tanggal=x)
    user_3_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_3, tanggal=x)
    
    user_4_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_4, tanggal=x)
    user_4_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_4, tanggal=x)
    user_4_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_4, tanggal=x)
    user_4_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_4, tanggal=x)
    user_4_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_4, tanggal=x)
    
    user_5_room_5_sch_1 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_1, user=user_5, tanggal=x)
    user_5_room_5_sch_2 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_2, user=user_5, tanggal=x)
    user_5_room_5_sch_3 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_3, user=user_5, tanggal=x)
    user_5_room_5_sch_4 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_4, user=user_5, tanggal=x)
    user_5_room_5_sch_5 = UserSchadule.objects.create(room=room_5, schadule=room_5_sch_5, user=user_5, tanggal=x)
    
    
    
    return redirect("home:home")


def delall(request):
    LevelAkun.objects.all().delete()
    Level.objects.all().delete()
    Kategori.objects.all().delete()
    Master.objects.all().delete()
    Setting.objects.all().delete()


    Kelas.objects.all().delete()
    Bab.objects.all().delete()
    Pelajaran.objects.all().delete()
    Questions.objects.all().delete()

    UserBab.objects.all().delete()
    UserCourse.objects.all().delete()
    UserLatihan.objects.all().delete()
    UserLesson.objects.all().delete()
    
    return redirect("home:home")