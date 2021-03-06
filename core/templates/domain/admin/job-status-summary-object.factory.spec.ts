// Copyright 2020 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Unit tests for JobSpecObjectFactory.ts.
 */

import { JobStausSummaryObjectFactory } from
  'domain/admin/job-status-summary-object.factory';

describe('Job Spec Object Factory', () => {
  let jsof: JobStausSummaryObjectFactory;

  beforeEach(() => {
    jsof = new JobStausSummaryObjectFactory();
  });

  it('should correctly convert backend dict to JobSpec object.', () => {
    let backendDict = {
      job_type: 'ActivityReferencesModelAuditOneOffJob',
      is_queued_or_running: false
    };

    let jobSpecObject = jsof.createFromBackendDict(backendDict);

    expect(jobSpecObject.jobType).toEqual(
      'ActivityReferencesModelAuditOneOffJob');
    expect(jobSpecObject.isQueuedOrRunning).toEqual(false);
  });
});
