--WITH READING CRIME SCENE REPORTS, FOUND THE TIME AND PLACE INFO ABOUT THE THEFT
SELECT year, month, day, street, description
FROM crime_scene_reports;

--|2021|7| 28| Humphrey Street|Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery. |

------------------------------------------

--WITH READING INTERVIEWS, FOUND THE CLUE ABOUT THE ESCAPE
SELECT name, year, month, day, transcript
FROM interviews;

--Ruth: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

--Eugene: I don't know the thief's name, but it was someone I recognized.
--Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money

--Raymond:As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--The thief then asked the person on the other end of the phone to purchase the flight ticket.

------------------------------------------

--WITH READING SECURITY_LOGS, FOUND THE LICENSES THAT EXIT PARKING LOT AFTER THE THEFT
SELECT hour, minute, activity, license_plate
FROM bakery_security_logs
WHERE year == 2021
AND month == 7
AND day == 28;

--| 10   | 16     | exit     | 5P2BI95       |
--| 10   | 18     | exit     | 94KL13X       |
--| 10   | 18     | exit     | 6P58WS2       |
--| 10   | 19     | exit     | 4328GD8       |
--| 10   | 20     | exit     | G412CB7       |
--| 10   | 21     | exit     | L93JTIZ       |
--| 10   | 23     | exit     | 322W7JE       |
--| 10   | 23     | exit     | 0NTHK55       |
--| 10   | 35     | exit     | 1106N58       |
--| 14   | 18     | exit     | NAW9653       |
--| 15   | 6      | exit     | RS7I6A0       |
--| 15   | 16     | exit     | 94MV71O       |
--| 16   | 6      | exit     | WD5M8I6       |
--| 16   | 38     | exit     | 4468KVT       |
--| 16   | 42     | exit     | 207W38T       |
--| 16   | 47     | exit     | C194752       |
--| 17   | 11     | exit     | NRYN856       |
--| 17   | 15     | exit     | 13FNH73       |
--| 17   | 16     | exit     | V47T75I       |
--| 17   | 18     | exit     | R3G7486       |
--| 17   | 36     | exit     | FLFN3W0       |
--| 17   | 47     | exit     | 4963D92       |

------------------------------------------

--WITH READING ATM LOGS, FOUND INFO ABOUT RELEVANT TRANSACTIONS AND BANK ACCOUNT
SELECT  amount, account_number
FROM atm_transactions
WHERE year == 2021
AND month == 7
AND day == 28
AND transaction_type == 'withdraw'
AND atm_location LIKE 'Humphrey%';

--| amount | account_number |
--+--------+----------------+
--| 45     | 90209473       |
--| 15     | 41935128       |
--| 55     | 66344537       |
--| 5      | 92647903       |
--| 35     | 40665580       |
--| 20     | 96336648       |
--| 20     | 69638157       |
--| 15     | 13156006       |
--| 40     | 89843009       |
--| 40     | 92647903       |
--| 55     | 57022441       |
--| 5      | 79165736       |
--| 10     | 76849114       |
--| 60     | 66344537       |
--| 100    | 50380485       |
--| 60     | 46222318       |
--| 10     | 58673910       |
--| 35     | 93903397       |
--| 65     | 79127781       |
--| 45     | 95773068       |
--| 35     | 26797365       |
--| 100    | 34939061       |
--| 50     | 65190958       |
--| 20     | 99031604       |
--| 30     | 58552019       |
--| 5      | 55322348       |

SELECT person_id, creation_year
FROM bank_accounts
WHERE account_number IN (SELECT account_number FROM atm_transactions
WHERE year == 2021 AND month == 7 AND day == 28
AND transaction_type == 'withdraw' AND atm_location LIKE 'Humphrey%');

--| person_id | creation_year |
--+-----------+---------------+
--| 779942    | 2010          |
--| 539960    | 2011          |
--| 985539    | 2011          |
--| 484375    | 2011          |
--| 632023    | 2011          |
--| 704850    | 2012          |
--| 757606    | 2012          |
--| 293753    | 2012          |
--| 572028    | 2012          |
--| 274388    | 2012          |
--| 567218    | 2012          |
--| 229572    | 2013          |
--| 652412    | 2013          |
--| 341739    | 2014          |
--| 713341    | 2015          |
--| 637069    | 2016          |
--| 630782    | 2016          |
--| 336397    | 2016          |
--| 769190    | 2017          |
--| 274893    | 2017          |
--| 929343    | 2017          |
--| 920334    | 2017          |
--| 837455    | 2018          |
--| 506435    | 2019          |

------------------------------------------

--WITH READING PHONE_CALLS, FOUND THE RELEVANT PHONE_CALLS
SELECT caller, receiver, duration
FROM phone_calls
WHERE year == 2021
AND month == 7
AND day == 28;

--|     caller     |    receiver    |
--+----------------+----------------+
--| (130) 555-0289 | (996) 555-8899 |
--| (499) 555-9472 | (892) 555-8872 |
--| (367) 555-5533 | (375) 555-8161 |
--| (609) 555-5876 | (389) 555-5198 |
--| (499) 555-9472 | (717) 555-1342 |
--| (286) 555-6063 | (676) 555-6554 |
--| (770) 555-1861 | (725) 555-3243 |
--| (031) 555-6622 | (910) 555-3251 |
--| (826) 555-1652 | (066) 555-9701 |
--| (338) 555-6650 | (704) 555-2131 |

------------------------------------------

--WITH READING AIRPORTS, FOUND THE INFO ABOUT FIFTYVILLE AIRPORT
SELECT id, abbreviation, full_name, city
FROM airports
WHERE city == 'Fiftyville';
--| 8  | CSF          | Fiftyville Regional Airport | Fiftyville |

--WITH READING FLIGHT INFO, FOUND THE RELEVANT FLIGHTS
SELECT id, destination_airport_id, hour, minute
FROM flights
WHERE year == 2021
AND month == 7
AND day == 28
AND hour >= 10
AND minute >= 15
AND origin_airport_id == 8
ORDER BY hour ASC;

--| id | destination_airport_id | hour | minute |
--+----+------------------------+------+--------+
--| 6  | 5                      | 13   | 49     |
--| 35 | 4                      | 16   | 16     |
--| 1  | 7                      | 17   | 50     |
--| 34 | 5                      | 17   | 20     |
--| 17 | 4                      | 20   | 16     |

--THIS IS THE FLIGHT THE THEFT WILL TAKE
--| 5  | DFS          | Dallas/Fort Worth International Airport | Dallas        |
--| 6  | 5                      | 13   | 49     |

------------------------------------------

--WITH READING PASSENGERS INFO, FOUND THE RELEVANT PASSENGERS
SELECT passport_number, seat
FROM passengers
WHERE flight_id == 6;

--| passport_number | seat |
--+-----------------+------+
--| 3835860232      | 9A   |
--| 1618186613      | 2C   |
--| 7179245843      | 3B   |
--| 1682575122      | 4B   |
--| 7597790505      | 5D   |
--| 6128131458      | 6B   |
--| 6264773605      | 7D   |
--| 3642612721      | 8A   |

------------------------------------------

--WITH USING PEOPLE INFO AND ALL OTHER INFO FROM PAST, FOUND THE THEFT AND ACCOMPLICE
SELECT id, name, phone_number
FROM people
WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year == 2021 AND month == 7 AND day == 28)
AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id == 6)
AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year == 2021 AND month == 7 AND day == 28 AND activity == 'exit');
--| 750165 | Daniel | (971) 555-6468 |

SELECT caller, receiver, duration
FROM phone_calls
WHERE year == 2021
AND month == 7
AND day == 28
AND caller == '(971) 555-6468';

------------------------------------------

SELECT id, name
FROM people
WHERE phone_number IN ('(971) 555-6468', '(267) 555-2761');
