/*
 * Copyright (c) 2024 SUSE LLC
 *
 * This software is licensed to you under the GNU General Public License,
 * version 2 (GPLv2). There is NO WARRANTY for this software, express or
 * implied, including the implied warranties of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
 * along with this software; if not, see
 * http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
 *
 * Red Hat trademarks are not licensed under GPLv2. No permission is
 * granted to use or replicate Red Hat trademarks that are incorporated
 * in this software or its documentation.
 */
package com.suse.manager.model.attestation;

import com.redhat.rhn.common.localization.LocalizationService;

public enum CoCoAttestationStatus {
    PENDING,
    SUCCEEDED,
    FAILED;

    private final String descriptionKey;

    CoCoAttestationStatus() {
        this.descriptionKey = "coco.status." + name().toLowerCase() + ".description";
    }

    public String getDescription() {
        return LocalizationService.getInstance().getMessage(descriptionKey);
    }
}
