# 2019 - IoT
# Sensor - Power Consumtpion Calculator


class Sensor:
    def __init__(self, name, resmin, resmax, datamin, datamax, wirpmin, wirpmax, num, adc):
        self.name = name
        self.resmin = resmin
        self.resmax = resmax
        self.datamin = datamin
        self.datamax = datamax
        self.wirpmin = wirpmin
        self.wirpmax = wirpmax
        self.num = num
        self.adc = adc



    def total_max_power(self):
        return 5 * self.datamax * 1e-9



s1 = Sensor('Heart Rate', 4, 12, 6700, 10000, 4.175e-05, 5e-05, 1, 5.5e-09)
s2 = Sensor('Humidity (capacitive)', 8, 16, 49.5, 66, 3.33e-07, 3.3e-07, 2, 0)
s3 = Sensor('Battery Monitor', 5, 8, 41.25, 55, 2.475e-07, 2.5e-07, 3, 0)
s4 = Sensor('Temprature', 6, 12, 100, 2020, 5e-07, 1e-06, 4, 6.6e-10)
s5 = Sensor('Accelerometer', 8, 14, 6600, 8080, 2.53e-05, 4.4e-05, 5, 3.6e-8)
s6 = Sensor('Magnetometer', 8, 16, 4950, 6600, 1.70e-05, 2.25e-05, 6, 1.0E-8)
s7 = Sensor('Altimeter/Pressure', 8, 24, 4950, 7425, 1.70e-05, 10.1, 7, 2.2e-8)
s8 = Sensor('Imager(VGA,RGB', 8, 10, 100000000, 1e+8, 4.17e-01, 0.2525, 8, 8.8e-4)
s9 = Sensor('Imager (MP4 compressed)', 8, 10, 17500000, 50500000, 1.70E-01, 2.53E-01, 9, 8.8e-4)
s10 = Sensor('Infared Proximity', 10, 16, 1750, 3400, 0.00000875, 1.70E-05, 10, 1.1e-8)
s11 = Sensor('Gyroscope', 12, 16, 10000, 175000, 5.00E-05, 0.001515, 11, 3.666e-6)
s12 = Sensor('Microphone', 12, 16, 505000, 670000, 2.53E-03, 0.003535, 12, 3.66e-4)
s13 = Sensor('CO2', 14, 16, 1750, 3400, 0.00000875, 1.29e-05, 13, 5.5e-10)
s14 = Sensor('Light', 16, 24, 925, 2575, 4.13E-06, 1.1e-06, 14, 6.6e-7)
s15 = Sensor('Strain', 16, 24, 175000, 340000, 4.63E-04, 1.29e-03, 15, 6.6e-5)
s16 = Sensor('Ultra-Violet', 16, 24, 1750, 3400, 0.00000875, 1.29e-05, 16, 2.2e-7)


def get_power(entry):
    if entry == s1.num:
        val = s1.total_max_power()
    elif entry == s2.num:
        val = s2.total_max_power()
    elif entry == s3.num:
        val = s3.total_max_power()
    elif entry == s4.num:
        val = s4.total_max_power()
    elif entry == s5.num:
        val = s6.total_max_power()
    elif entry == s7.num:
        val = s7.total_max_power()
    elif entry == s8.num:
        val = s8.total_max_power()
    elif entry == s9.num:
        val = s9.total_max_power()
    elif entry == s10.num:
        val = s10.total_max_power()
    elif entry == s11.num:
        val = s11.total_max_power()
    elif entry == s12.num:
        val = s12.total_max_power()
    elif entry == s13.num:
        val = s13.total_max_power()
    elif entry == s14.num:
        val = s14.total_max_power()
    elif entry == s15.num:
        val = s15.total_max_power()
    else:
        val = s16.total_max_power()
    # else:
    # print('Invalid Input... Try again!')

    return val


def get_adc(entry):
    if entry == s1.num:
        val = s1.adc
    elif entry == s2.num:
        val = s2.adc
    elif entry == s3.num:
        val = s3.adc
    elif entry == s4.num:
        val = s4.adc
    elif entry == s5.num:
        val = s6.adc
    elif entry == s7.num:
        val = s7.adc
    elif entry == s8.num:
        val = s8.adc
    elif entry == s9.num:
        val = s9.adc
    elif entry == s10.num:
        val = s10.adc
    elif entry == s11.num:
        val = s11.adc
    elif entry == s12.num:
        val = s12.adc
    elif entry == s13.num:
        val = s13.adc
    elif entry == s14.num:
        val = s14.adc
    elif entry == s15.num:
        val = s15.adc
    else:
        val = s16.adc
    # else:
    # print('Invalid Input... Try again!')

    return val


print('\n\n\n\n')

print(
    '██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗███████╗████████╗     ██████╗ ███████╗    ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ███████╗')
print(
    '██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝    ██╔═══██╗██╔════╝    ╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ ██╔════╝')
print(
    '██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║█████╗     ██║       ██║   ██║█████╗         ██║   ███████║██║██╔██╗ ██║██║  ███╗███████╗')
print(
    '██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝     ██║       ██║   ██║██╔══╝         ██║   ██╔══██║██║██║╚██╗██║██║   ██║╚════██║')
print(
    '██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║███████╗   ██║       ╚██████╔╝██║            ██║   ██║  ██║██║██║ ╚████║╚██████╔╝███████║')
print(
    '╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝        ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝')
print('\t' * 30 + '╔═╗┬ ┬┌┐┌┌┬┐┌─┐┬┌─┌─┐┌─┐')
print('\t' * 30 + '╚═╗└┬┘│││ │ ├─┤├┴┐├─┤└─┐')
print('\t' * 30 + '╚═╝ ┴ ┘└┘ ┴ ┴ ┴┴ ┴┴ ┴└─┘')
print('          \tSensors:\n')
print(
    '\t1.  \tHeart Rate\n\t2.  \tHumidity (capacitive)\n\t3.  \tBattery Monitor\n\t4.  \tTemprature\n\t5.  '
    '\tAccelerometer\n\t6. '
    '   \tMagnetometer\n\t7.  \tAltimeter/Pressure\n\t8.  \tImager (VGA, RGB)\n\t9.  \tImager (MP4 compressed)\n\t10. '
    '\tInfrared '
    'Proximity\n\t11. \tGyroscope\n\t12. \tMicrophone\n\t13. \tCO2\n\t14. \tLight\n\t15. \tStrain\n\t16. '
    '\tUltra-Violet\n')

print('Give the sensors number as input OR type "q" if you want to calculate the power of the chosen sensors)')
print('Sensors ID <----> Number listed Order')

print('===========================================================================================================')
print('    ____  ____ _       ____________     _____ _______   _______ ____  ____     _________    __    ______')
print('   / __ \/ __ \ |     / / ____/ __ \   / ___// ____/ | / / ___// __ \/ __ \   / ____/   |  / /   / ____/')
print('  / /_/ / / / / | /| / / __/ / /_/ /   \__ \/ __/ /  |/ /\__ \/ / / / /_/ /  / /   / /| | / /   / / ')
print(' / ____/ /_/ /| |/ |/ / /___/ _, _/   ___/ / /___/ /|  /___/ / /_/ / _, _/  / /___/ ___ |/ /___/ /___')
print('/_/    \____/ |__/|__/_____/_/ |_|   /____/_____/_/ |_//____/\____/_/ |_|   \____/_/  |_/_____/\____/  ')

IDlist = []
adclist = []


# flag = True
def calc_power():
    IDlist = []
    adclist = []
    while 1:
        id = input('Select a sensor from the list - - - (press "q" to finish selection) :\n')
        if id == 'q':
            break
        po = get_power(int(id))
        IDlist.append(po)
        adpo = get_adc(int(id))
        adclist.append(adpo)

    # print(IDlist)
    PowerTotal = sum(IDlist)

    AdcPowerTo = sum(adclist)

    totalPower = PowerTotal + AdcPowerTo

    print(
        f'The Power consumed by the chosen Sensors is:\n\n\t   \t{PowerTotal} W due to max Datarate range and Wireless Power\n\t   \t{AdcPowerTo} W due to ADC power consumption\n\t   \t\nAdding to a total max Power of : \t{totalPower} W\n')


def ex():
    while 1:
        com = input('To exit type "done" :')
        if com == 'done':
            break


while 1:
    command = input('Press "A" to calculate power OR any key to exit :\n')

    if command == 'A':
        calc_power()
        print('\n\n')
        print(
            '██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗███████╗████████╗     ██████╗ ███████╗    ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ███████╗')
        print(
            '██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝    ██╔═══██╗██╔════╝    ╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ ██╔════╝')
        print(
            '██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║█████╗     ██║       ██║   ██║█████╗         ██║   ███████║██║██╔██╗ ██║██║  ███╗███████╗')
        print(
            '██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝     ██║       ██║   ██║██╔══╝         ██║   ██╔══██║██║██║╚██╗██║██║   ██║╚════██║')
        print(
            '██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║███████╗   ██║       ╚██████╔╝██║            ██║   ██║  ██║██║██║ ╚████║╚██████╔╝███████║')
        print(
            '╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝        ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝')
        print(
            '===========================================================================================================')
        print(
            '    ____  ____ _       ____________     _____ _______   _______ ____  ____     _________    __    ______')
        print(
            '   / __ \/ __ \ |     / / ____/ __ \   / ___// ____/ | / / ___// __ \/ __ \   / ____/   |  / /   / ____/')
        print('  / /_/ / / / / | /| / / __/ / /_/ /   \__ \/ __/ /  |/ /\__ \/ / / / /_/ /  / /   / /| | / /   / / ')
        print(' / ____/ /_/ /| |/ |/ / /___/ _, _/   ___/ / /___/ /|  /___/ / /_/ / _, _/  / /___/ ___ |/ /___/ /___')
        print('/_/    \____/ |__/|__/_____/_/ |_|   /____/_____/_/ |_//____/\____/_/ |_|   \____/_/  |_/_____/\____/  ')
    else:
        ex()
        break
