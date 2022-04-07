import deepdiff
import pytest
import requests
from lib.base_class import BaseClass
from deepdiff import DeepDiff
import json

class TestUserAgent(BaseClass):

    agents_from_base_class = BaseClass.agents

    @pytest.mark.parametrize('agent', agents_from_base_class)
    def test_get_user_agent(self, agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"User-Agent":agent}

        response = requests.get(url, headers=data)

        if agent == BaseClass.agents[0]:
            values_from_response = response.text
            ser_to_json = json.loads(values_from_response)

            diff = deepdiff.DeepDiff(BaseClass.expected_values_0,ser_to_json, exclude_regex_paths="user_agent")
            assert diff == {}, f"Error! Invalid values received: {diff}"

        if agent == BaseClass.agents[1]:
            values_from_response = response.text
            ser_to_json = json.loads(values_from_response)

            diff = deepdiff.DeepDiff(BaseClass.expected_values_1,ser_to_json, exclude_regex_paths="user_agent")
            assert diff == {}, f"Error! Invalid values received: {diff}"

        if agent == BaseClass.agents[2]:
            values_from_response = response.text
            ser_to_json = json.loads(values_from_response)

            diff = deepdiff.DeepDiff(BaseClass.expected_values_2,ser_to_json, exclude_regex_paths="user_agent")
            assert diff == {}, f"Error! Invalid values received: {diff}"

        if agent == BaseClass.agents[3]:
            values_from_response = response.text
            ser_to_json = json.loads(values_from_response)

            diff = deepdiff.DeepDiff(BaseClass.expected_values_3,ser_to_json, exclude_regex_paths="user_agent")
            assert diff == {}, f"Error! Invalid values received: {diff}"

        if agent == BaseClass.agents[4]:
            values_from_response = response.text
            ser_to_json = json.loads(values_from_response)

            diff = deepdiff.DeepDiff(BaseClass.expected_values_4,ser_to_json, exclude_regex_paths="user_agent")
            assert diff == {}, f"Error! Invalid values received: {diff}"