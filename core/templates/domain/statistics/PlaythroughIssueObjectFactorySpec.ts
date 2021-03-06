// Copyright 2018 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Unit tests for the PlaythroughIssueObjectFactory.
 */

import {
  IPlaythroughIssueBackendDict,
  PlaythroughIssueObjectFactory,
  EarlyQuitPlaythroughIssue
} from 'domain/statistics/PlaythroughIssueObjectFactory';

describe('Playthrough Issue Object Factory', () => {
  let piof: PlaythroughIssueObjectFactory;
  let playthroughIssueObject: EarlyQuitPlaythroughIssue;
  beforeEach(() => {
    piof = new PlaythroughIssueObjectFactory();
  });

  it('should create a new exploration issue', () => {
    playthroughIssueObject = new EarlyQuitPlaythroughIssue(
      'EarlyQuit', {
        state_name: {
          value: 'state'
        },
        time_spent_in_exp_in_msecs: {
          value: 1.2
        }
      }, [], 1, true);

    expect(playthroughIssueObject.issueType).toEqual('EarlyQuit');
    expect(playthroughIssueObject.issueCustomizationArgs).toEqual({
      state_name: {
        value: 'state'
      },
      time_spent_in_exp_in_msecs: {
        value: 1.2
      }
    });
    expect(playthroughIssueObject.playthroughIds).toEqual([]);
    expect(playthroughIssueObject.schemaVersion).toEqual(1);
    expect(playthroughIssueObject.isValid).toEqual(true);
  });

  it('should create a new exploration issue from a backend dict', () => {
    const playthroughIssueObject = piof.createFromBackendDict({
      issue_type: 'EarlyQuit',
      issue_customization_args: {
        state_name: {
          value: 'state'
        },
        time_spent_in_exp_in_msecs: {
          value: 1.2
        }
      },
      playthrough_ids: [],
      schema_version: 1,
      is_valid: true
    });

    expect(playthroughIssueObject.issueType).toEqual('EarlyQuit');
    expect(playthroughIssueObject.issueCustomizationArgs).toEqual( {
      state_name: {
        value: 'state'
      },
      time_spent_in_exp_in_msecs: {
        value: 1.2
      }
    });
    expect(playthroughIssueObject.playthroughIds).toEqual([]);
    expect(playthroughIssueObject.schemaVersion).toEqual(1);
    expect(playthroughIssueObject.isValid).toEqual(true);
  });

  it('should convert exploration issue to backend dict', () => {
    const playthroughDict: IPlaythroughIssueBackendDict = {
      issue_type: 'EarlyQuit',
      issue_customization_args: {
        state_name: {
          value: 'state'
        },
        time_spent_in_exp_in_msecs: {
          value: 1.2
        }
      },
      playthrough_ids: [],
      schema_version: 1,
      is_valid: true
    };
    const playthroughIssueObject = piof.createFromBackendDict(playthroughDict);

    expect(playthroughIssueObject.toBackendDict()).toEqual(playthroughDict);
  });

  it('should throw error on invalid backend dict', () => {
    const playthroughDict = {
      issue_type: 'InvalidType',
      issue_customization_args: {
        state_name: {
          value: 'state'
        },
        time_spent_in_exp_in_msecs: {
          value: 1.2
        }
      },
      playthrough_ids: [],
      schema_version: 1,
      is_valid: true
    };

    expect(() => {
      // TS ignore is used because playthrough dict is assigned a invalid type
      // to test errors.
      // @ts-ignore
      piof.createFromBackendDict(playthroughDict);
    }).toThrowError(
      'Backend dict does not match any known issue type: ' +
      JSON.stringify(playthroughDict));
  });
});
