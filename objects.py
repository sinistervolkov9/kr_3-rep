# Обработка данных из json-файла и приведение к необходимому виду

from datetime import datetime


class Operation:
    def __init__(self,
                 transaction_id: int,
                 date,
                 state,
                 operation_amount,
                 description,
                 out_from,
                 to
                 ):
        self.transaction_id = transaction_id
        self.date = self.date_converter(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.out_from = self.payment_info_converter(out_from)
        self.to = self.payment_info_converter(to)

    def date_converter(self, date):
        """
        Приводит заданную в json-файле дату
        к необходимому виду
        :param date: пример: 2018-06-30T02:08:58.425572
        :return: пример: 30.06.2018
        """
        date_list = []

        day = date[8:10]
        month = date[5:7]
        year = date[:4]

        date_list.append(day)
        date_list.append(month)
        date_list.append(year)

        correct_date = ''.join(date_list)

        #return correct_date

        return datetime.strptime(correct_date, '%d%m%Y').date()


    def payment_info_converter(self, info_payment):
        """
        pass
        :param info_payment:
        :return:
        """
        # MasterCard 8532498887072395)
        # Visa Platinum 7000 79** **** 6361

        if info_payment:
            info_payment_list = info_payment.split(" ")
            if info_payment.startswith("Счет"):
                info_payment_number = info_payment_list.pop(-1)
                correct_info_payment = f"**{info_payment_number[-4:]}"
                info_payment_list.append(correct_info_payment)
            else:
                info_payment_number = info_payment_list.pop(-1)
                correct_info_payment_number_list = []
                for i in range(len(info_payment_number) + 1):
                    if i == 4:
                        correct_info_payment_number_list.append(info_payment_number[i - 4:i])
                    elif i == 6:
                        correct_info_payment_number_list.append(info_payment_number[i - 2:i] + "**")
                    elif i == 12 or i == 16:
                        correct_info_payment_number_list.append(info_payment_number[i - 4:i])
                correct_info_payment_number_list[2] = "****"

                info_payment_list.extend(correct_info_payment_number_list)

            return " ".join(info_payment_list)
        return ""

    def __repr__(self):
        return f"{self.date} {self.description}\n{self.out_from} -> {self.to}\n{self.operation_amount['amount']} {self.operation_amount['currency']['name']}\n"