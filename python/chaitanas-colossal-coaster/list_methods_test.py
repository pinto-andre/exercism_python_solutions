import unittest
import pytest
from copy import deepcopy

from list_methods import (
    add_me_to_the_queue,
    find_my_friend,
    add_me_with_my_friends,
    remove_the_mean_person,
    how_many_namefellows,
    remove_the_last_person,
    sorted_names,
)


class ListMethodsTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue(self):
        test_data = [
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 0, "HawkEye"),
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich"),
        ]
        result_data = [["RobotGuy", "WW", "HawkEye"], ["Tony", "Bruce", "RichieRich"]]

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):

            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            express_queue, normal_queue, ticket_type, person_name = deepcopy(params)

            with self.subTest(
                f"variation #{variant}",
                express_queue=express_queue,
                normal_queue=normal_queue,
                ticket_type=ticket_type,
                person_name=person_name,
                expected=expected,
            ):

                actual_result = add_me_to_the_queue(*params)
                error_message = (
                    f"Called add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}. "
                    f"The function returned {actual_result}, but "
                    f"The tests expected {expected} when adding "
                    f"{person_name} to the queue."
                )

                self.assertListEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_find_my_friend(self):
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Natasha"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Steve"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Rocket"),
        ]
        result_data = (0, 1, 4)

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):
            with self.subTest(
                f"variation #{variant}", params=params, expected=expected
            ):
                actual_result = find_my_friend(*params)
                error_message = (
                    f"Called find_my_friend{params}. "
                    f"The function returned {actual_result}, but "
                    f"The tests expected {expected} when looking for "
                    f"{params[-1]} in the queue."
                )

                self.assertIs(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends(self):
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 0, "Bucky"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 1, "Bucky"),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 5, "Bucky"),
        ]

        result_data = [
            ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket", "Bucky"],
        ]

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):

            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            queue, index, person_name = deepcopy(params)

            with self.subTest(
                f"variation #{variant}",
                queue=queue,
                index=index,
                person_name=person_name,
                expected=expected,
            ):

                actual_result = add_me_with_my_friends(*params)
                error_message = (
                    f"Called add_me_with_my_friends{queue, index, person_name}. "
                    f"The function returned {actual_result}, but "
                    f"The tests expected {expected} when adding "
                    f"{person_name} to position {index} in the queue."
                )

                self.assertListEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person(self):
        test_data = [
            (["Natasha", "Steve", "Ultron", "Wanda", "Rocket"], "Ultron"),
            (["Natasha", "Steve", "Wanda", "Rocket", "Ultron"], "Ultron"),
            (["Ultron", "Natasha", "Steve", "Wanda", "Rocket"], "Ultron"),
        ]
        result_data = [
            ["Natasha", "Steve", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Wanda", "Rocket"],
            ["Natasha", "Steve", "Wanda", "Rocket"],
        ]

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):

            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            queue, person_name = deepcopy(params)

            with self.subTest(
                f"variation #{variant}",
                queue=queue,
                person_name=person_name,
                expected=expected,
            ):

                actual_result = remove_the_mean_person(*params)
                error_message = (
                    f"Called remove_the_mean_person{queue, person_name}. "
                    f"The function returned {actual_result}, but "
                    f"The tests expected {expected} when removing "
                    f"{person_name} from the queue."
                )

                self.assertListEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows(self):
        test_data = [
            (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Bucky"),
            (["Natasha", "Steve", "Ultron", "Rocket"], "Natasha"),
            (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Natasha"),
        ]

        result_data = (0, 1, 2)

        for variant, (params, expected) in enumerate(
            zip(test_data, result_data), start=1
        ):
            with self.subTest(
                f"variation #{variant}", params=params, expected=expected
            ):
                actual_result = how_many_namefellows(*params)

                error_message = (
                    f"Called how_many_namefellows{params}. "
                    f"The function returned {actual_result}, but "
                    f"The tests expected {expected} when counting "
                    f"namefellows in the queue for {params[-1]}."
                )

                self.assertIs(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_remove_the_last_person(self):
        test_data = ["Natasha", "Steve", "Ultron", "Natasha", "Rocket"]
        actual_result = remove_the_last_person(test_data)
        expected = "Rocket"
        error_message = (
            f"Called remove_the_last_person({test_data})."
            f"The function returned {actual_result}, but the tests "
            f"expected {expected} as the person who was removed."
        )

        self.assertIs(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=7)
    def test_sorted_names(self):
        test_data = ["Steve", "Ultron", "Natasha", "Rocket"]
        expected = ["Natasha", "Rocket", "Steve", "Ultron"]
        actual_result = sorted_names(test_data)
        error_message = (
            f"Called sorted_names({test_data})."
            f"The function returned {actual_result}, but the tests "
            f"expected {expected}."
        )

        self.assertListEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=8)
    def test_only_accepts_strings(self):
        test_data = [
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 0, 1),
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 1, True),
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 1, -0.5),
        ]

        for variant, (
            express_queue,
            normal_queue,
            ticket_type,
            person_name,
        ) in enumerate(test_data, start=1):
            with self.subTest(
                f"variation #{variant}",
                express_queue=express_queue,
                normal_queue=normal_queue,
                ticket_type=ticket_type,
                person_name=person_name,
            ):
                with pytest.raises(TypeError):
                    add_me_to_the_queue(
                        express_queue, normal_queue, ticket_type, person_name
                    )

    @pytest.mark.task(taskno=9)
    def test_only_accepts_0_and_1(self):
        test_data = [
            (["Tony", "Bruce"], ["RobotGuy", "WW"], -2, "RobotGuy"),
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 2, "RobotGuy"),
            (["Tony", "Bruce"], ["RobotGuy", "WW"], 0.5, "RobotGuy"),
        ]

        for variant, (
            express_queue,
            normal_queue,
            ticket_type,
            person_name,
        ) in enumerate(test_data, start=1):
            with self.subTest(
                f"variation #{variant}",
                express_queue=express_queue,
                normal_queue=normal_queue,
                ticket_type=ticket_type,
                person_name=person_name,
            ):
                with pytest.raises(ValueError):
                    add_me_to_the_queue(
                        express_queue, normal_queue, ticket_type, person_name
                    )

    @pytest.mark.task(taskno=10)
    def test_find_my_friend_only_accepts_strings_friends_names(self):
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 1),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], True),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], ["Rocket", -1, False]),
        ]

        for variant, (queue, friend_name) in enumerate(test_data, start=1):
            with self.subTest(
                f"variation #{variant}", queue=queue, friend_name=friend_name
            ):
                with pytest.raises(TypeError):
                    find_my_friend(queue, friend_name)

    @pytest.mark.task(taskno=11)
    def test_add_me_with_my_friends_only_accepts_int_index_and_str_person_name(self):
        test_data = [
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Bucky", 0),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], True, False),
            (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], False, -0.5),
        ]

        for variant, (queue, index, person_name) in enumerate(test_data, start=1):
            with self.subTest(
                f"variation #{variant}",
                queue=queue,
                index=index,
                person_name=person_name,
            ):
                with pytest.raises(TypeError):
                    add_me_with_my_friends(queue, index, person_name)
